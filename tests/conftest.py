import pytest
import pytest_asyncio
from httpx import AsyncClient, ASGITransport
from src.main import app
from src.database import database, engine, metadata

from src.config import settings

settings.database = ""


@pytest_asyncio.fixture(scope="function", autouse=True)
async def setup_database():
    """Fixture para configurar o banco de dados de teste"""
    # Cria as tabelas usando SQLAlchemy (forma síncrona)
    metadata.create_all(engine)
    
    # Conecta ao banco usando databases
    if not database.is_connected:
        await database.connect()
    
    # CRIAR USUÁRIO DE TESTE
    try:
        await database.execute(
            """
            INSERT INTO users (id, name, email) 
            VALUES (1, 'Test User', 'test@example.com')
            """
        )
    except Exception as e:
        print(f"Erro ao criar usuário: {e}")
        # Usuário já existe, continua
        pass
    
    yield
    
    # Desconecta do banco
    if database.is_connected:
        await database.disconnect()
    
    # Remove todas as tabelas
    metadata.drop_all(engine)


@pytest_asyncio.fixture(scope="function")
async def db():
    """Fixture que retorna a conexão do banco"""
    return database


@pytest_asyncio.fixture(scope="function")
async def client():
    """Fixture para criar cliente HTTP de teste"""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        yield ac


@pytest_asyncio.fixture(scope="function")
async def access_token(client: AsyncClient):
    """Fixture para obter token de acesso"""
    response = await client.post("/auth/login", json={"user_id": "1"})
    data = response.json()
    print(f"Token response: {data}")  # Debug
    print(f"Status code: {response.status_code}")  # Debug
    return data["access_token"]
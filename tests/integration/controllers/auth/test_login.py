from fastapi import status
from httpx import AsyncClient

# Teste de integração para o endpoint de login
async def test_login_success(client: AsyncClient):
    # Dados de login válidos
    data = {"user_id": "1"}
    # Faz a requisição POST para o endpoint de login
    response = await client.post("/auth/login", json=data)
    # Verifica se a resposta está correta
    assert response.status_code == status.HTTP_200_OK
    # Verifica se o token de acesso está presente na resposta
    assert response.json()["access_token"] is not None

            
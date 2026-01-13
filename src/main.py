from contextlib import asynccontextmanager 
from fastapi.responses import JSONResponse
from src.exceptions import NotFoundPostError
from fastapi import FastAPI, status, Request
from src.controllers import auth, post
from src.model.post import posts
from fastapi.middleware.cors import CORSMiddleware
from src.database import database 

# 1. Configuração do Ciclo de Vida (Banco de Dados)
@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect() # Conecta ao iniciar
    yield
    await database.disconnect() # Desconecta ao encerrar

# 2. Metadados e Servidores
tags_metadata = [
    {"name": "auth", "description": "Operação para autenticação."},
    {"name": "posts", "description": "Operação para manter posts."},
]

servers = [
    {"url": "http://127.0.0.1:8000", "description": "Local development"},
]

# 3. Criação da instância ÚNICA do FastAPI
app = FastAPI(
    title="blog API",
    version="1.2.0",
    summary="Api para blog pessoal.",
    description="""API para blog pessoal. Suporta CRUD completo da tabel posts.""",
    openapi_tags=tags_metadata,
    servers=servers,
    lifespan=lifespan # <--- O lifespan deve entrar AQUI
)

# 4. Middlewares
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 5. Handler de Exceção
@app.exception_handler(NotFoundPostError)
async def not_found_post_exception_handler(request: Request, exc: NotFoundPostError):
    return JSONResponse(
        status_code=exc.status_code,
        content={"detail": exc.message},
    )

# 6. Inclusão das Rotas (Registrando no app configurado)
app.include_router(auth.router, tags=["auth"])
app.include_router(post.router, tags=["posts"])

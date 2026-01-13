import sqlalchemy as sa
from src.database import metadata, database
from fastapi import APIRouter
from pydantic import BaseModel

# Tabela de usuários
users = sa.Table(
    "users",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True, autoincrement=True),
    sa.Column("name", sa.String(100), nullable=False),
    sa.Column("email", sa.String(100), nullable=False, unique=True),
    sa.Column("created_at", sa.DateTime, server_default=sa.func.now()),
)

# Tabela de posts 
posts = sa.Table(
    "posts",
    metadata,
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("title", sa.String(150), nullable=False, unique=True),
    sa.Column("content", sa.String(100), nullable=False),
    sa.Column("published_at", sa.DateTime, nullable=True),
    sa.Column("published", sa.Boolean, nullable=False),
)
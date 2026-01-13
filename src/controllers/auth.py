from fastapi import APIRouter

from src.schemas.post.auth import LoginIn 
from src.security import sign_jwt
from src.views.post.auth import LoginOut

router = APIRouter(prefix="/auth")
# Rota para login de usuário
@router.post("/login", response_model=LoginOut)
async def login(data: LoginIn):
    return sign_jwt(user_id=data.user_id)
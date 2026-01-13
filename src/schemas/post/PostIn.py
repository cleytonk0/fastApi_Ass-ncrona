from datetime import datetime

from pydantic import BaseModel
# Modelo Pydantic para entrada de dados ao criar um post
class PostIn(BaseModel):
    # Modelagem dos dados de entrada para criação de post
    # Atributos do post
    title:str
    content:str
    published_at: datetime | None = None
    published: bool = False
from fastapi import APIRouter, Depends, HTTPException, status
from src.Service.Post import PostService
from src.database import database
from src.schemas.post.PostIn import PostIn
from src.schemas.post.PostUpdatein import PostUpdateIn
from src.security import login_required
from src.views.post.PostOut import PostOut
from src.model.post import posts

router = APIRouter(prefix="/posts", dependencies=[Depends(login_required)])

service = PostService()

@router.get("/", response_model=list[PostOut])
async def read_posts(published: str, limit: int, skip: int = 0):
    # Converter "on"/"off" para booleano
    is_published = published.lower() == "on"
    
    # Construir query com filtros
    query = posts.select().where(
        posts.c.published == is_published
    ).limit(limit).offset(skip)
    
    return await database.fetch_all(query)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostOut)
async def create_post(post: PostIn):
    comand = posts.insert().values(
        title=post.title,
        content=post.content,
        published_at=post.published_at,
        published=post.published,
    )
      
    last_id = await database.execute(comand)
    
    result = {**post.model_dump(), "id": last_id}

    return result
  
  
  
@router.get("/{id}", response_model=PostOut)
async def read_post(id: int):
    return await service.read(id)


@router.patch("/{id}", response_model=PostOut)
async def update_post(id: int, post: PostUpdateIn):
   
    return await service.update(id, post)
   
@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_post(id: int):
    await service.delete(id)
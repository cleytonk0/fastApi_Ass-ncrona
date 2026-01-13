from src.exceptions import NotFoundPostError
from src.database import database
from databases.interfaces import Record
from src.model.post import posts
from src.schemas.post import PostIn, PostUpdatein

# Service para operações relacionadas a posts
class PostService:
    # Lê todos os posts com paginação
    async def read_all(self, published: bool, limit: int, skip: int = 0) -> list[Record]:
        query = posts.select().limit(limit).offset(skip)
        return await database.fetch_all(query)
    # Lê um post específico por ID
    async def create(self, post: PostIn) -> int:
        command = posts.insert().values(
            title=post.title,
            content=post.content,
            published_at=post.published_at,
            published=post.published,
        )
        return await database.execute(command)
    # Conta o número de posts
    async def read(self, id: int) -> Record:
        return await self.__get_by_id(id)
    # Conta o número de posts por ID
    async def update(self, id: int, post: PostUpdatein) -> Record:
        total = await self.count(id)
        if not total:
            raise NotFoundPostError
        data = post.model_dump(exclude_unset=True)
        command = posts.update().where(posts.c.id == id).values(**data)
        await database.execute(command)

        return await self.__get_by_id(id)
    # Método para deletar um post por ID
    async def delete(self, id: int) -> None:
        total = await self.count(id)
        if not total:
            raise NotFoundPostError
        command = posts.delete().where(posts.c.id == id)
        await database.execute(command)
    # Método para contar posts por ID
    async def count(self, id: int) -> int:
        query = "select count(id) as total from posts where id = :id"
        result = await database.fetch_one(query, {"id": id})
        return result.total
    # Método privado para obter um post por ID
    async def __get_by_id(self, id: int) -> Record:
        query = posts.select().where(posts.c.id == id)
        post = await database.fetch_one(query)
        if not post:
            raise NotFoundPostError
        return post

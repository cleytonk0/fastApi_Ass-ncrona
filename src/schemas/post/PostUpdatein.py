from datetime import datetime

from pydantic import BaseModel

class PostIn(BaseModel):
    title: str
    content: str
    published: bool = False
    published_at: datetime | None = None

class PostUpdateIn(BaseModel):
    title: str | None = None
    content: str | None = None
    published: bool | None = None
    published_at: datetime | None = None
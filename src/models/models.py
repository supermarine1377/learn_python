from pydantic import BaseModel

class Post(BaseModel):
    """
    JSONPlaceholderの投稿データを表す。
    """
    userId: int
    id: int
    title: str
    body: str

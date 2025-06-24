from typing import TypedDict

class Post(TypedDict):
    """
    JSONPlaceholderの投稿データを表す。
    """
    userId: int
    id: int
    title: str
    body: str
import requests
from src.learn_python.models.models import Post

_API_BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_posts() -> list[Post]:
    """
    Fetches posts from the JSONPlaceholder API.
    
    Returns:
        list[Post]: A list of posts.
    """
    response = requests.get(f"{_API_BASE_URL}/posts")
    response.raise_for_status()  # Raise an error for bad responses

    raw_post_data = response.json()
    posts = [Post.model_validate(post) for post in raw_post_data]
    return posts
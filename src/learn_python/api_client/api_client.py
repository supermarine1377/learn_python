import requests
from learn_python.models.models import Post
class APIClient:
    """
    A client for interacting with the JSONPlaceholder API.
    """
    def __init__(self, base_url: str):
        self._base_url = base_url
        self._session = requests.Session()
    
    def fetch_posts(self) -> list[Post]:
        """
        Fetches posts from the JSONPlaceholder API.
        
        Returns:
            list[Post]: A list of posts.
        """
        response = self._session.get(f"{self._base_url}/posts")
        response.raise_for_status()

        raw_post_data = response.json()
        posts = [Post.model_validate(post) for post in raw_post_data]

        return posts

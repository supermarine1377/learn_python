from learn_python.api_client.api_client import APIClient

_API_BASE_URL = "https://jsonplaceholder.typicode.com"

def main():
  try:
    api_client = APIClient(base_url=_API_BASE_URL)
    posts = api_client.fetch_posts()
    for post in posts:
        print(f"Title: {post.title}, Body: {post.body}")
  except Exception as e:
    print(f"Error fetching posts: {e}")

if __name__ == "__main__":
    main()
from src.learn_python.api_client.api_client import fetch_posts

def main():
  try:
    posts = fetch_posts()
    for post in posts:
        print(f"Title: {post['title']}, Body: {post['body']}")
  except Exception as e:
    print(f"Error fetching posts: {e}")

if __name__ == "__main__":
    main()
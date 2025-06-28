from learn_python.api_client.api_client import ApiClient
from learn_python.writers.csv import CsvWriter

_API_BASE_URL = "https://jsonplaceholder.typicode.com"

def main():
  try:
    api_client = ApiClient(base_url=_API_BASE_URL)
    posts = api_client.fetch_posts()

  except Exception as e:
    print(f"Error fetching posts: {e}")
  
  posts_dict = [post.model_dump() for post in posts]

  try:
    csv_writer = CsvWriter()
    csv_writer.write("posts.csv", posts_dict)
    print("CSV file written successfully.")
  except Exception as e:
    print(f"Error writing CSV file: {e}")

if __name__ == "__main__":
    main()
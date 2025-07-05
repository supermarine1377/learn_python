from api_client.api_client import ApiClient
from writers.csv import CsvWriter
import argparse

_API_BASE_URL = "https://jsonplaceholder.typicode.com"

def parse_path_arg() -> str:
  parser = argparse.ArgumentParser(description="The file path to write the CSV file.")
  parser.add_argument("--output", default="post.csv", help="The file path to write the CSV file.")
  return parser.parse_args().output

def main():
  path = parse_path_arg()

  try:
    api_client = ApiClient(base_url=_API_BASE_URL)
    posts = api_client.fetch_posts()

  except Exception as e:
    print(f"Error fetching posts: {e}")
  
  posts_dict = [post.model_dump() for post in posts]

  try:
    csv_writer = CsvWriter()
    csv_writer.write(path, posts_dict)
    print("CSV file written successfully.")
  except Exception as e:
    print(f"Error writing CSV file: {e}")

if __name__ == "__main__":
    main()
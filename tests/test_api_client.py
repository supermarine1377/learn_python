import pytest
from pytest_mock import MockerFixture
from learn_python.api_client.api_client import APIClient
from learn_python.models.models import Post
import requests

dummy_api_url = "http://dummy.com"

def test_get_posts_success(mocker: MockerFixture):

  dummy_posts_data = [
    {"userId": 1, "id": 1, "title": "Test Title 1", "body": "Test Body 1"},
    {"userId": 1, "id": 2, "title": "Test Title 2", "body": "Test Body 2"},
  ]

  mock_response = mocker.Mock()
  mock_response.raise_for_status.return_value = None
  mock_response.json.return_value = dummy_posts_data

  mocker.patch(
    "requests.Session.get", 
    return_value=mock_response
  )

  client = APIClient(base_url=dummy_api_url)
  posts = client.fetch_posts()

  assert len(posts) == 2
  assert isinstance(posts[0], Post)
  assert posts[0].title == "Test Title 1"
  assert posts[0].id == 1
  assert posts[0].title == "Test Title 1"
  assert posts[0].body == "Test Body 1"
  assert posts[1].title == "Test Title 2"
  assert posts[1].id == 2
  assert posts[1].title == "Test Title 2"
  assert posts[1].body == "Test Body 2"

  requests.Session.get.assert_called_once_with(f"{dummy_api_url}/posts")

def test_get_posts_failure(mocker: MockerFixture):
  mock_response = mocker.Mock()
  mock_response.raise_for_status.side_effect = requests.exceptions.HTTPError

  mocker.patch(
    "requests.Session.get",
    return_value=mock_response
  )

  client = APIClient(base_url=dummy_api_url)

  with pytest.raises(requests.exceptions.HTTPError):
    client.fetch_posts()
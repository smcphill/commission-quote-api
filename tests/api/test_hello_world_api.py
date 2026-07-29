import requests


def test_index_returns_hello_world():
    response = requests.get("http://localhost:5000/")
    assert response.status_code == 200
    assert "<h1>Hello World</h1>" in response.text

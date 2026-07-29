from app.main import app


def test_index_returns_hello_world():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"<h1>Hello World</h1>" in response.data

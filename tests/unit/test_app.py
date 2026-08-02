from app.main import app


def test_index_returns_commission_quote_heading():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"<h1>Commission Quote</h1>" in response.data

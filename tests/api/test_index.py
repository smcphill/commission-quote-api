import requests


def test_index_returns_commission_quote_heading(base_url):
    response = requests.get(f"{base_url}/")
    assert response.status_code == 200
    assert "<h1>Commission Quote</h1>" in response.text

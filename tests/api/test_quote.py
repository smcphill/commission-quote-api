import requests


def test_request_quote_returns_commission_quote(base_url):
    payload = {
        "loanAmount": 50000,
        "loanTermInMonths": 24,
        "riskBand": "AVERAGE",
    }

    response = requests.post(f"{base_url}/api/quote", json=payload)

    assert response.status_code == 200
    body = response.json()
    assert body == {
        "quoteId": "123",
        "commissionRate": 0.1,
        "totalCommission": 100000,
    }

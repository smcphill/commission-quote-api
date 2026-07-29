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


def test_request_quote_with_no_data_raises(base_url):
    response = requests.post(f"{base_url}/api/quote", json={})

    assert response.status_code == 400
    assert response.json() == {"error": "Missing request"}


def test_request_quote_with_invalid_risk_band_raises(base_url):
    payload = {
        "loanAmount": 50000,
        "loanTermInMonths": 24,
        "riskBand": "bananas",
    }
    response = requests.post(f"{base_url}/api/quote", json=payload)

    assert response.status_code == 400
    assert response.json() == {"error": "Invalid riskBand"}

import pytest
from app.main import generate_quote, QuoteRequest

RISK_BAND_UNUSED = [
    ("BELOW_AVERAGE", 100),
    ("AVERAGE", 100),
    ("VERY_GOOD", 100),
    ("EXCELLENT", 100),
]


@pytest.mark.parametrize("risk_band, expected_commission", RISK_BAND_UNUSED)
def test_generate_quote_does_not_use_risk_band(risk_band, expected_commission):
    quote_request = QuoteRequest(
        loanAmount=1000,
        loanTermInMonths=12,
        riskBand=risk_band,
    )
    total_commission = generate_quote(quote_request).get("totalCommission")
    assert total_commission == expected_commission

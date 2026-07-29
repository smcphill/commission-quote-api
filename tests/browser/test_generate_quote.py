def test_generate_quote_with_invalid_risk_band_shows_error(page, base_url):
    page.goto(f"{base_url}/")

    page.fill("#loanAmount", "50000")
    page.fill("#loanTermInMonths", "24")
    page.eval_on_selector(
        "#riskBand",
        "(select) => { select.insertAdjacentHTML('beforeend', '<option value=\"bananas\">bananas</option>'); select.value = 'bananas'; }",
    )
    page.click("button[type=submit]")

    status = page.locator("#quote-status")
    page.wait_for_function(
        "document.getElementById('quote-status').textContent !== 'Generating quote…'"
    )

    assert status.inner_text() == "Failed to generate quote: Invalid riskBand"
    assert page.locator("#quote-result").is_hidden()


def test_generate_quote_happy_path(page, base_url):
    page.goto(f"{base_url}/")

    page.fill("#loanAmount", "50000")
    page.fill("#loanTermInMonths", "24")
    page.select_option("#riskBand", "AVERAGE")
    page.click("button[type=submit]")

    result = page.locator("#quote-result")
    result.wait_for(state="visible")

    assert page.locator("#quote-id").inner_text() == "123"
    assert page.locator("#quote-commission-rate").inner_text() == "0.1"
    assert page.locator("#quote-total-commission").inner_text() == "100000"
    assert page.locator("#quote-status").inner_text() == ""

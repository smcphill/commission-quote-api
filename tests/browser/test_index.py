def test_index_renders_commission_quote_heading(page, base_url):
    page.goto(f"{base_url}/")
    assert page.locator("h1").inner_text() == "Commission Quote"

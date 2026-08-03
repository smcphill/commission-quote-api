def test_index_renders_commission_quote_heading(page, base_url):
    page.goto(f"{base_url}/")
    assert page.locator("h1").inner_text() == "Commission Quote"


def test_index_does_not_render_dev_mode_by_default(page, base_url):
    page.goto(f"{base_url}/")
    assert page.locator("#dev-mode").is_hidden()
    assert page.locator("#chaosMode").is_hidden()
    assert page.locator("#apiKey").is_hidden()


def test_index_does_renders_dev_mode_when_requested(page, base_url):
    page.goto(f"{base_url}/?use=dev")
    assert page.locator("#dev-mode").is_visible()
    assert page.locator("#chaosMode").is_visible()
    assert page.locator("#apiKey").is_visible()

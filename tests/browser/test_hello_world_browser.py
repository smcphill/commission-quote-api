from playwright.sync_api import sync_playwright


def test_index_renders_hello_world():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto("http://localhost:5000/")
        assert page.locator("h1").inner_text() == "Hello World"
        browser.close()

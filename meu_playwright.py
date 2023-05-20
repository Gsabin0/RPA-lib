from playwright.sync_api import sync_playwright


def conf_playwright(url, visualizar=None):
    if visualizar is None:
        v = False
    else:
        v = visualizar
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=v)
        page = browser.new_page()
        page.goto(url)
        
    return page


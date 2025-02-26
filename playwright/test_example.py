import re
from playwright.sync_api import Playwright, sync_playwright, expect
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page()
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://guu.ru/")
    page.get_by_role("link", name="Внеучебная деятельность").click()
    page.screenshot(path="screenshot.png")

    # ---------------------
    context.close()
    browser.close()
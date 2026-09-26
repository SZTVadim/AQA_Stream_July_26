# Для установки playwright команда "pip install playwright"
# pytest и playwright вместе, pip install pytest-playwright
import pytest
from playwright.sync_api import Page, expect, sync_playwright, BrowserContext


def test_ui(page: Page):
    page.goto("https://lahtajunior.ru/services/service-to-pediatr")

    expect(page.get_by_role("button", name="Записаться онлайн", exact=True)).to_be_visible()

def test_disabled(page: Page):
    page.goto("https://www.qa-practice.com/elements/button/disabled")

    expect(page.locator("#submit-id-submit")).to_be_disabled()

    page.locator("[name='select_state']").select_option("Enabled")

    expect(page.locator("#submit-id-submit")).to_be_enabled()


def test_orange(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    page.locator("[name='select_state']").fill("test")
    page.fill("//input","test")
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    expect(page).to_have_title("OrangeHRM")

def test_login(page: Page):
    page.goto("https://opensource-demo.orangehrmlive.com/")
    page.get_by_placeholder("Username").fill("Admin")
    page.get_by_placeholder("Password").fill("admin123")
    page.get_by_role("button", name="Login").click()
    expect(page).to_have_url("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")

# Чтобы запустить playwright самостоятельно, надо сделать самим фикстуры:
"""
@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture(scope="function")
def browser(playwright_instance):
    # browser = playwright_instance.chromium.launch(headless=False, slow_mo=50)  # slow_mo помогает видеть шаги
    browser = playwright_instance.chromium.launch(headless=True)
    yield browser
    browser.close()


@pytest.fixture(scope="function")
def context(browser):
    context = browser.new_context()
    try:
        yield context
    finally:
        context.close()


@pytest.fixture(scope="function")
def page(context: BrowserContext) -> Page:
    page = context.new_page()
    # page.set_viewport_size({'width': 1920, 'height': 1080})
    return page
"""


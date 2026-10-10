import pytest
from playwright.sync_api import sync_playwright

from lessons.UI_project.config.credentials import PASSWORD, USERNAME
from lessons.UI_project.pages.auth_page import AuthPage
from lessons.UI_project.pages.dashboard_page import DashboardPage


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture
def browser(playwright_instance):
    # browser = playwright_instance.chromium.launch(headless=True)
    browser = playwright_instance.chromium.launch(headless=False, slow_mo=1000)  # чтобы видеть шаги
    yield browser
    browser.close()

@pytest.fixture
def context(browser):
    context = browser.new_context()
    try:
        yield context
    finally:
        context.close()

@pytest.fixture
def page(context):
    return context.new_page()


@pytest.fixture
def auth_page(page):
    auth_page = AuthPage(page)
    auth_page.open_page(auth_page.PAGE_URL)
    return auth_page


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)

@pytest.fixture
def dashboard(auth_page, dashboard_page):
    auth_page.authorize_on_site(USERNAME, PASSWORD)
    return dashboard_page
import pytest
from playwright.sync_api import sync_playwright

from config.credentials import USERNAME, PASSWORD
from pages.auth_page import AuthPage
from pages.dashboard_page import DashboardPage
from pages.pim.add_employee_pge import AddEmployee
from pages.pim.employee_list_page import EmployeeList
from pages.pim.personal_details_page import PersonalDetailsPage


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p

@pytest.fixture
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True)
    # browser = playwright_instance.chromium.launch(headless=False, slow_mo=2000) # slowmo помогает видеть шаги
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
    page = context.new_page()
    # page.set_viewport_size(1920, 1080)
    return page

@pytest.fixture
def auth_page(page) -> AuthPage:
    auth_page = AuthPage(page)
    auth_page.open_page(auth_page.PAGE_URL)
    return auth_page


@pytest.fixture
def dashboard_page(page):
    return DashboardPage(page)

@pytest.fixture
def dashboard(auth_page: AuthPage, dashboard_page: DashboardPage) -> DashboardPage:
    auth_page.authorize(USERNAME, PASSWORD)
    return dashboard_page

@pytest.fixture
def employee_list_page(page):
    return EmployeeList(page)

@pytest.fixture
def add_employee_page(page):
    return AddEmployee(page)

@pytest.fixture
def personal_details(page):
    return PersonalDetailsPage(page)



import allure
from playwright.sync_api import expect

from config.credentials import USERNAME, PASSWORD


class TestAuthorize:
    @allure.title("Авторизация")
    def test_authorize(self, auth_page, dashboard_page):
        auth_page.authorize(USERNAME, PASSWORD)
        expect(dashboard_page.page).to_have_url(dashboard_page.full_url(dashboard_page.PAGE_URL))
        expect(dashboard_page.header_control.header_locator).to_have_text("Dashboard")

    @allure.title("Проверка элементов на странице")
    def test_visible_elements(self, auth_page):
        expect(auth_page.submit_locator()).to_be_visible()
        expect(auth_page.username_locator()).to_be_visible()
        expect(auth_page.header_locator()).to_be_visible()
        expect(auth_page.password_locator()).to_be_visible()
        expect(auth_page.copyright_wrapper_locator()).to_be_visible()

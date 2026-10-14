import re

import pytest
from playwright.sync_api import expect

from lessons.UI_project.config.credentials import USERNAME, PASSWORD


class TestAuthorize:
    @pytest.mark.smoke
    def test_visible_elements(self, auth_page):
        expect(auth_page.page).to_have_url(re.compile("auth/login"))
        expect(auth_page.page).to_have_title("OrangeHRM")

        expect(auth_page.header_locator).to_have_text("Login")
        expect(auth_page.password_locator).to_be_visible()
        expect(auth_page.username_locator).to_be_visible()
        expect(auth_page.copyright_wrapper_locator).to_be_visible()
        expect(auth_page.submit_locator).to_be_visible()
        expect(auth_page.forgot_password_locator).to_be_visible()

    @pytest.mark.regression
    @pytest.mark.parametrize("username,password", [(USERNAME, "invalid_password"), ("invalid_username", PASSWORD)],
                             ids=["invalid_password", "invalid_username"])
    def test_invalid_credentials(self, auth_page, username, password):
        auth_page.fill_username(username)
        auth_page.fill_password(password)
        auth_page.click_login()
        expect(auth_page.invalid_credentials_locator).to_be_visible()

    def test_authorize(self, auth_page, dashboard_page):
        auth_page.authorize_on_site(USERNAME, PASSWORD)

        expect(dashboard_page.page).to_have_url(dashboard_page.full_url(dashboard_page.PAGE_URL))
        expect(dashboard_page.header_control.header_locator).to_have_text("Dashboard")

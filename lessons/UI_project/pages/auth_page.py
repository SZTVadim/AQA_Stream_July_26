from lessons.UI_project.pages.base_page import BasePage


class AuthPage(BasePage):
    PAGE_URL = "auth/login"

    # селекторы
    _header_selector = ".orangehrm-login-title"
    _username_selector = "[name=username]"
    _password_selector = "[name=password]"
    _submit_selector = "[type=submit]"
    _forgot_password_selector = ".orangehrm-login-forgot-header"
    _copyright_wrapper_selector = ".orangehrm-copyright-wrapper"
    _invalid_credentials_selector = ".oxd-alert-content-text"

    # локаторы
    @property
    def header_locator(self):
        return self.element(self._header_selector)

    @property
    def username_locator(self):
        return self.element(self._username_selector)

    @property
    def password_locator(self):
        return self.element(self._password_selector)

    @property
    def submit_locator(self):
        return self.element(self._submit_selector)

    @property
    def forgot_password_locator(self):
        return self.element(self._forgot_password_selector)

    @property
    def copyright_wrapper_locator(self):
        return self.element(self._copyright_wrapper_selector)

    @property
    def invalid_credentials_locator(self):
        return self.element(self._invalid_credentials_selector)

    # методы
    def fill_username(self, username):
        self.username_locator.fill(username)

    def fill_password(self, password):
        self.password_locator.fill(password)

    def click_login(self):
        self.submit_locator.click()

    # комбинированные методы
    def authorize_on_site(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login()

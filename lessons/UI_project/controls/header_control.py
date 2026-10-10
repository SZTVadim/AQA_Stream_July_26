from playwright.sync_api import Page


class HeaderControl:
    def __init__(self, page: Page):
        self.page = page


    # селекторы
    _header_selector = ".oxd-topbar-header-title"
    _upgrade_button_selector = ".orangehrm-upgrade-button"
    _user_menu_selector = "div.oxd-topbar-header-userarea"
    _about_from_menu_selector = "//*[text()='About']"
    _support_from_menu_selector = "//*[text()='Support']"
    _change_password_from_menu_selector = "//*[text()='Change Password']"
    _logout_from_menu_selector = "//*[text()='Logout']"
    _help_from_menu_selector = "//*[@title='Help']"

    # локаторы
    @property
    def header_locator(self):
        return self.page.locator(self._header_selector)

    @property
    def upgrade_button_locator(self):
        return self.page.locator(self._upgrade_button_selector)

    @property
    def user_menu_locator(self):
        return self.page.locator(self._user_menu_selector)

    @property
    def about_from_menu_locator(self):
        return self.page.locator(self._about_from_menu_selector)

    @property
    def support_from_menu_locator(self):
        return self.page.locator(self._support_from_menu_selector)

    @property
    def change_password_from_menu_locator(self):
        return self.page.locator(self._change_password_from_menu_selector)

    @property
    def logout_from_menu_locator(self):
        return self.page.locator(self._logout_from_menu_selector)

    @property
    def help_from_menu_locator(self):
        return self.page.locator(self._help_from_menu_selector)

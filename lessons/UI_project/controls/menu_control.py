from playwright.sync_api import Page


class MenuControl:
    def __init__(self, page: Page):
        self.page = page

    # селекторы
    _logo_selector = "[alt='client brand banner']"
    _search_input_selector = "[placeholder='Search']"
    _admin_selector = "//*[text()='Admin']/.."
    _pim_selector = "//*[text()='PIM']/.."
    _leave_selector = "//*[text()='Leave']/.."
    _time_selector = "//*[text()='Time']/.."
    _dashboard_selector = "//*[text()='Dashboard']/.."
    _recruitment_selector = "//*[text()='Recruitment']/.."
    _my_info_selector = "//*[text()='My Info']/.."
    _performance_selector = "//*[text()='Performance']/.."
    _directory_selector = "//*[text()='Directory']/.."
    _maintenance_selector = "//*[text()='Maintenance']/.."
    _claim_selector = "//*[text()='Claim']/.."
    _buzz_selector = "//*[text()='Buzz']/.."
    _collapse_menu_selector = ".oxd-main-menu-button"

    #локаторы
    @property
    def logo_locator(self):
        return self.page.locator(self._logo_selector)

    @property
    def search_input_locator(self):
        return self.page.locator(self._search_input_selector)

    @property
    def admin_locator(self):
        return self.page.locator(self._admin_selector)

    @property
    def pim_locator(self):
        return self.page.locator(self._pim_selector)

    @property
    def leave_locator(self):
        return self.page.locator(self._leave_selector)

    @property
    def time_locator(self):
        return self.page.locator(self._time_selector)

    @property
    def dashboard_locator(self):
        return self.page.locator(self._dashboard_selector)

    @property
    def recruitment_locator(self):
        return self.page.locator(self._recruitment_selector)

    @property
    def my_info_locator(self):
        return self.page.locator(self._my_info_selector)

    @property
    def performance_locator(self):
        return self.page.locator(self._performance_selector)

    @property
    def directory_locator(self):
        return self.page.locator(self._directory_selector)

    @property
    def maintenance_locator(self):
        return self.page.locator(self._maintenance_selector)

    @property
    def claim_locator(self):
        return self.page.locator(self._claim_selector)

    @property
    def buzz_locator(self):
        return self.page.locator(self._buzz_selector)

    @property
    def collapse_menu_locator(self):
        return self.page.locator(self._collapse_menu_selector)

    # методы
    def open_dashboard(self):
        self.dashboard_locator.click()

    def open_admin(self):
        self.admin_locator.click()

    def open_pim(self):
        self.pim_locator.click()
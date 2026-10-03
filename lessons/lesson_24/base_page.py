from playwright.sync_api import expect, Page


class BasePage:
    __BASE_URL = "https://opensource-demo.orangehrmlive.com"
    _PATH_URL = "/web/index.php/"

    def __init__(self, page: Page):
        self.page = page
        self._endpoint = ''

    def _get_full_url(self):
        return f"{self.__BASE_URL}/{self._PATH_URL}/{self._endpoint}"

    def navigate_to(self):
        full_url = self._get_full_url()
        self.page.goto(full_url)
        self.page.wait_for_load_state('load')
        # expect(self.page).to_have_url(full_url)

    def wait_for_selector_and_fill(self, username_selector, username):
        element = self.page.locator(username_selector)
        element.fill(username)

    def wait_for_selector_and_click(self, element):
        expect(element).to_be_visible()
        element.click()
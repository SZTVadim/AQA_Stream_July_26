from playwright.sync_api import Page


class BasePage:
    BASE_URL = "https://opensource-demo.orangehrmlive.com"
    PATH_URL = "web/index.php"

    def __init__(self, page: Page):
        self.page = page

    def full_url(self, url, id_user=None):
        if id_user:
            return f"{self.BASE_URL}/{self.PATH_URL}/{url}/{id_user}"
        return f"{self.BASE_URL}/{self.PATH_URL}/{url}"

    def open_page(self, url, id_user=None):
        self.page.goto(self.full_url(url, id_user))

    def element(self, selector):
        return self.page.locator(selector)

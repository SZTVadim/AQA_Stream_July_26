import allure
from playwright.sync_api import expect


class TestDashboard:
    @allure.title("Проверка элементов на странице")
    def test_visible_elements(self, dashboard):
        expect(dashboard.buzz_latest_posts_locator()).to_be_visible()
        expect(dashboard.my_actions_locator()).to_be_visible()
        expect(dashboard.time_at_work_locator()).to_be_visible()
        expect(dashboard.quick_launch_locator()).to_be_visible()


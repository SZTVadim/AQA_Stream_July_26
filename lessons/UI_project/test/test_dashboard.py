from playwright.sync_api import expect


class TestDashboard:
    def test_visible_element(self, dashboard):
        expect(dashboard.buzz_latest_pasts_locator).to_be_visible()
        expect(dashboard.my_action_locator).to_be_visible()
        expect(dashboard.time_at_work_locator).to_be_visible()
        expect(dashboard.quick_launch_locator).to_be_visible()
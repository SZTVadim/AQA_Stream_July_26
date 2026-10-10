from lessons.UI_project.pages.personal_page import PersonalPage


class DashboardPage(PersonalPage):
    PAGE_URL = "dashboard/index"

    # cселекторы
    _time_at_work_selector = "//i[contains(@class, 'bi-clock-fill')]/../../.."
    _my_action_selector = "//i[contains(@class, 'bi-list-check')]/../../.."
    _quick_launch_selector = "//i[contains(@class, 'bi-lightning-charge-fill')]/../../.."
    _buzz_latest_pasts_selector = "//i[contains(@class, 'bi-camera-fill')]/../../.."

        # локаторы
    @property
    def time_at_work_locator(self):
        return self.element(self._time_at_work_selector)

    @property
    def my_action_locator(self):
        return self.element(self._my_action_selector)

    @property
    def quick_launch_locator(self):
        return self.element(self._quick_launch_selector)

    @property
    def buzz_latest_pasts_locator(self):
        return self.element(self._buzz_latest_pasts_selector)

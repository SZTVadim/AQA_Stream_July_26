from lessons.UI_project.pages.pim_page import PimPage


class EmployeeListPage(PimPage):
    PAGE_URL = "pim/viewEmployeeList"

    # селекторы
    _add_button_selector = "//*[contains(@class, 'bi-plus')]/.."

    # локаторы
    @property
    def add_button_locator(self):
        return self.element(self._add_button_selector)

    # методы
    def click_add_button(self):
        self.add_button_locator.click()

        

from lessons.UI_project.pages.pim_page import PimPage
from lessons.UI_project.utils.employee_generator import Employee


class AddEmployeePage(PimPage):
    PAGE_URL = "pim/addEmployee"

    #селекторы
    _add_employee_title_selector = ".orangehrm-main-title"
    _first_name_input_selector = ".orangehrm-firstname"
    _middle_name_input_selector = ".orangehrm-middlename"
    _last_name_input_selector = ".orangehrm-lastname"
    _employee_id_selector = "//*[contains(@class,'oxd-grid-2')]//input[contains(@class,'oxd-input')]"
    _cancel_button_selector = ".oxd-button--ghost"
    _save_button_selector = ".oxd-button--secondary"

    #локаторы
    @property
    def add_employee_title_locator(self):
        return self.element(self._add_employee_title_selector)

    @property
    def first_name_input_locator(self):
        return self.element(self._first_name_input_selector)

    @property
    def middle_name_input_locator(self):
        return self.element(self._middle_name_input_selector)

    @property
    def last_name_input_locator(self):
        return self.element(self._last_name_input_selector)

    @property
    def employee_id_locator(self):
        return self.element(self._employee_id_selector)

    @property
    def cancel_button_locator(self):
        return self.element(self._cancel_button_selector)

    @property
    def save_button_locator(self):
        return self.element(self._save_button_selector)

    # методы
    def fill_first_name(self, first_name):
        self.first_name_input_locator.fill(first_name)

    def fill_middle_name(self, middle_name):
        self.middle_name_input_locator.fill(middle_name)

    def fill_last_name(self, last_name):
        self.last_name_input_locator.fill(last_name)

    def fill_employee_id(self, employee_id):
        self.employee_id_locator.fill(employee_id)

    def click_save_button(self):
        self.save_button_locator.click()

    def click_cancel_button(self):
        self.cancel_button_locator.click()

    # комбинированные методы
    def add_employee(self, employee: Employee):
        self.fill_first_name(employee.first_name)
        self.fill_middle_name(employee.middle_name)
        self.fill_last_name(employee.last_name)
        self.fill_employee_id(employee.employee_id)
        self.click_save_button()
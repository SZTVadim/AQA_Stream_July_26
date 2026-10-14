from lessons.UI_project.pages.personal_page import PersonalPage


class PimPage(PersonalPage):
    PAGE_URL = "pim/viewEmployeeList"

    # селекторы
    _employee_list_selector = "//*[text()='Employee List']"
    _add_employee_selector = "//*[text()='Add Employee']"
    _report_selector = "//*[text()='Reports']"
    _configuration_selector = "//*[text()='Configuration ']"
    _optional_fields_selector = "//*[text()='Optional Fields']"
    _custom_fields_selector = "//*[text()='Custom Fields']"
    _data_import_selector = "//*[text()='Data Import']"
    _reporting_method_selector = "//*[text()='Reporting Methods']"
    _termination_reasons_selector = "//*[text()='Termination Reasons']"

    # локаторы
    @property
    def employee_list_locator(self):
        return self.element(self._employee_list_selector)

    @property
    def add_employee_locator(self):
        return self.element(self._add_employee_selector)

    @property
    def report_locator(self):
        return self.element(self._report_selector)

    @property
    def configuration_locator(self):
        return self.element(self._configuration_selector)

    @property
    def optional_fields_locator(self):
        return self.element(self._optional_fields_selector)

    @property
    def custom_fields_locator(self):
        return self.element(self._custom_fields_selector)

    @property
    def data_import_locator(self):
        return self.element(self._data_import_selector)

    @property
    def reporting_method_locator(self):
        return self.element(self._reporting_method_selector)

    @property
    def termination_reasons_locator(self):
        return self.element(self._termination_reasons_selector)

    # методы
    def open_add_employee(self):
        self.add_employee_locator.click()
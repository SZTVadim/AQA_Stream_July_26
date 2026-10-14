from lessons.UI_project.pages.pim_page import PimPage


class PersonalDetailsPage(PimPage):
    PAGE_URL = "pim/viewPersonalDetails/empNumber"

    # селекторы
    _title_selector = "//h6[text()='Personal Details']"
    _first_name_selector= "[name='firstName']"
    _last_name_selector= "[name='lastName']"
    _middle_name_selector= "[name='middleName']"

    # локаторы
    @property
    def title_locator(self):
        return self.element(self._title_selector)

    @property
    def first_name_locator(self):
        return self.element(self._first_name_selector)

    @property
    def last_name_locator(self):
        return self.element(self._last_name_selector)

    @property
    def middle_name_locator(self):
        return self.element(self._middle_name_selector)

import re

from playwright.sync_api import expect


class TestAddEmployee:
    def test_add_employee(self, dashboard, add_employee_page, employee_list_page, personal_details_page, employee_data):
        dashboard.menu_control.open_pim()
        employee_list_page.click_add_button()
        add_employee_page.open_page(add_employee_page.PAGE_URL)

        add_employee_page.add_employee(employee_data)

        expect(personal_details_page.title_locator).to_be_visible()
        expect(personal_details_page.page).to_have_url(re.compile(personal_details_page.PAGE_URL))

        expect(personal_details_page.last_name_locator).to_have_value(employee_data.last_name)
        expect(personal_details_page.middle_name_locator).to_have_value(employee_data.middle_name)
        expect(personal_details_page.first_name_locator).to_have_value(employee_data.first_name)
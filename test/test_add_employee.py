import random
import re

import allure
from playwright.sync_api import expect


class TestAddEmployee:
    @allure.title("Добавление работника")
    def test_add_employee(self, dashboard, employee_list_page, add_employee_page, personal_details):
        dashboard.manu_control.open_pim()
        employee_list_page.open_add_employee()
        add_employee_page.fill_form("test_first", "test_middle", "test_last", str(random.randint(1000000, 9999999)))
        expect(personal_details.page.locator("//h6[text()='Personal Details']")).to_have_text("Personal Details")
        expect(personal_details.page).to_have_url(re.compile("pim/viewPersonalDetails/empNumber/"))

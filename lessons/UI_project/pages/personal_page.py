from lessons.UI_project.controls.header_control import HeaderControl
from lessons.UI_project.controls.menu_control import MenuControl
from lessons.UI_project.pages.base_page import BasePage


class PersonalPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.menu_control = MenuControl(self.page)
        self.header_control = HeaderControl(self.page)
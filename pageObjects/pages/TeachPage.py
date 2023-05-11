from Helper import Helper
from pageObjects.locators.TeachLocators import TeachLocators


class TeachPage(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = TeachLocators()

    def delete_all_cookie(self):
        self.delete_all_cookies()

    def assert_find_main_banner(self):
        assert self.get_locator_by_xpath(self.elements.MAIN_BANNER)

    def click_get_started(self):
        self.click_button(self.elements.GET_START_BUTTON)

    def assert_modal_window_is_displayed(self):
        assert self.get_locator_by_xpath(self.elements.BECOME_INSTRUCTOR)

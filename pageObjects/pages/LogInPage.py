import time

from Helper import Helper
from pageObjects.locators.LogInLocators import LogInLocators


class LogInPage(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = LogInLocators()

    def click_google_button(self):
        self.click_button(self.elements.GOOGLE_BUTTON)

    def switch_to_google(self):
        self.switch_to_new_window()

    def assert_google_title(self):
        text = self.get_locator_by_xpath(self.elements.GOOGLE_TITLE).text
        assert text == "Вход"

    def click_facebook_button(self):
        self.click_button(self.elements.FACEBOOK_BUTTON)

    def assert_facebook_page(self):
        assert self.waiting_disappearance_element(self.elements.MODAL_FACEBOOK)

    def click_apple_button(self):
        self.click_button(self.elements.APPLE_BUTTON)

    def assert_apple_title(self):
        text = self.get_locator_by_xpath(self.elements.APPLE_TITLE).text
        assert text == "Apple ID"

    def click_log_in(self):
        self.click_button(self.elements.LOG_IN_BUTTON)

    def assert_page_not_change(self):
        assert (
            self.current_url()
            == "https://www.udemy.com/join/login-popup/?persist_locale=&locale=en_US"
        )

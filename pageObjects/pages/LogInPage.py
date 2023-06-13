import allure

from Helper import Helper
from pageObjects.locators.LogInLocators import LogInLocators


class LogInPage(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = LogInLocators()

    @allure.step("clicked google button")
    def click_google_button(self):
        self.click_button(self.elements.GOOGLE_BUTTON)

    @allure.step("switched to google page")
    def switch_to_google(self):
        self.switch_to_new_window()

    @allure.step("checked google page is opened")
    def assert_google_title(self):
        text = self.get_locator_by_xpath(self.elements.GOOGLE_TITLE).text
        assert text == "Вход"

    @allure.step("clicked facebook button")
    def click_facebook_button(self):
        self.click_button(self.elements.FACEBOOK_BUTTON)

    @allure.step("facebook page is opened")
    def assert_facebook_page(self):
        assert self.waiting_disappearance_element(self.elements.MODAL_FACEBOOK)

    @allure.step("clicked apple button")
    def click_apple_button(self):
        self.click_button(self.elements.APPLE_BUTTON)

    @allure.step("checked apple page opened")
    def assert_apple_title(self):
        text = self.get_locator_by_xpath(self.elements.APPLE_TITLE).text
        assert text == "Apple ID"

    @allure.step("clicked log in button")
    def click_log_in(self):
        self.click_button(self.elements.LOG_IN_BUTTON)

    @allure.step("checked url address")
    def assert_page_not_change(self):
        assert (
            self.current_url()
            == "https://www.udemy.com/join/login-popup/?persist_locale=&locale=en_US"
        )

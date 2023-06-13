import allure

from Helper import Helper
from pageObjects.locators.SingUpLocators import SingUpLocators


class SingUpPage(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = SingUpLocators()

    @allure.step("clicked 'sing up' button")
    def click_sing_up(self):
        self.click_button(self.elements.SING_UP_BUTTON)

    @allure.step("asserted registration form")
    def assert_registration_form(self):
        assert self.get_locator_by_xpath(self.elements.REGISTRATION_FORM)

    @allure.step("filled registration form")
    def fill_registration_form(self):
        self.send_keys(self.elements.FULL_NAME_INPUT, "Yauheni Hraudzin")
        self.send_keys(self.elements.EMAIL_INPUT, "ev.evv@gmail.com")
        self.send_keys(self.elements.PASSWORD, "Na12My34")

    @allure.step("checked url")
    def assert_change_page(self):
        assert self.current_url() == "https://www.udemy.com/"

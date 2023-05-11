from Helper import Helper
from pageObjects.locators.SingUpLocators import SingUpLocators


class SingUpPage(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = SingUpLocators()

    def click_sing_up(self):
        self.click_button(self.elements.SING_UP_BUTTON)

    def assert_registration_form(self):
        assert self.get_locator_by_xpath(self.elements.REGISTRATION_FORM)
from Helper import Helper
from pageObjects.locators.BusinessLocators import BusinessLocators


class BusinessPage(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = BusinessLocators()

    def assert_logo_is_displayed(self):
        assert self.get_locator_by_xpath(self.elements.BUSINESS_LOGO)

    def click_on_logo(self):
        self.click_button(self.elements.BUSINESS_LOGO)

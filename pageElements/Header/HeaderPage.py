from Helper import Helper
from pageElements.Header.HeaderLocators import HeaderLocators


class HeaderPage(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = HeaderLocators()

    def find_element_logo(self):
        assert self.get_locator_by_xpath(self.elements.LOGO)

    def click_on_logo(self):
        self.click_button(self.elements.LOGO)

    def check_url(self):
        assert self.current_url() == 'https://www.udemy.com/'

    def find_categories(self):
        self.get_locator_by_xpath(self.elements.CATEGORIES)

    def mouse_moving_to_categories(self):
        self.mouse_moving(HeaderLocators.CATEGORIES)

    def find_element_sub_categories(self):
        assert self.get_locator_by_xpath(HeaderLocators.SUB_CATEGORIES)
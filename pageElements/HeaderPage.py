from Helper import Helper
from pageObjects.HeaderObject import HeaderObject


class HeaderPage(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = HeaderObject()

    def waiting_logo(self):
        self.waiting_element(self.elements.LOGO)

    def find_element(self):
        assert self.get_locator_by_xpath(self.elements.LOGO)

    def click_on_logo(self):
        self.click_button(self.elements.LOGO)

    def url(self):
        assert self.current_url() == 'https://www.udemy.com/?persist_locale=&locale=en_US'

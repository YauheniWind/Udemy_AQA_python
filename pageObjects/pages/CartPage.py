from pageObjects.locators.CartLocators import CartLocators
from Helper import Helper


class CartPage(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = CartLocators()

    def check_url(self):
        assert self.current_url() != "https://www.udemy.com/course/bestpython/"

    def click_buy_now(self):
        self.click_button(self.elements.BUY_NOW_BUTTON)

    def assert_cart_info(self):
        assert self.get_locator_by_xpath(self.elements.LEAD_TITLE)
        assert self.get_locator_by_xpath(self.elements.PRICE, 2)
        assert self.get_locator_by_xpath(self.elements.PRICE, 0)
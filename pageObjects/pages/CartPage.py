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
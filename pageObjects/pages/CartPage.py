from pageObjects.locators.CartLocators import CartLocators
from Helper import Helper


class CartPage(Helper):

    def __init__(self, driver):
        super().__init__(driver)

        self.elements = CartLocators()


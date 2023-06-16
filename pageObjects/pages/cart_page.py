import allure

from pageObjects.locators.CartLocators import CartLocators
from Helper import Helper


class CartPage(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = CartLocators()

    @allure.step("checked url")
    def check_url(self):
        assert self.current_url() != "https://www.udemy.com/course/bestpython/"

    @allure.step("clicked 'buy now' button")
    def click_buy_now(self):
        self.click_button(self.elements.BUY_NOW_BUTTON)

    @allure.step("asserted cart info is displayed")
    def assert_cart_info(self):
        assert self.get_locator_by_xpath(self.elements.LEAD_TITLE)
        assert self.get_locator_by_xpath(self.elements.PRICE, 2)
        assert self.get_locator_by_xpath(self.elements.PRICE, 0)
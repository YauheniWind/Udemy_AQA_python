from Helper import Helper
from pageElements.MainPage.MainPageLocators import MainPageLocators

class MainPage(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = MainPageLocators()

    # Header
    def find_element_logo(self):
        assert self.get_locator_by_xpath(self.elements.LOGO)

    def click_on_logo(self):
        self.click_button(self.elements.LOGO)

    def check_url(self):
        assert self.current_url() == "https://www.udemy.com/"

    def find_categories(self):
        self.get_locator_by_xpath(self.elements.CATEGORIES)

    def mouse_moving_to_categories(self):
        self.mouse_moving(self.elements.CATEGORIES)

    def find_element_sub_categories(self):
        assert self.get_locator_by_xpath(self.elements.SUB_CATEGORIES)

    # Body

    def click_yes(self):
        self.click_button(self.elements.PRIVACY)

    def click_accept(self):
        self.click_button(self.elements.ACCEPT_PRIVACY)

    def scroll_to_skill_hub(self):
        self.scroll_to_element(self.elements.SKILLS_HUB)

    def click_on_second_button(self):
        self.click_button(self.elements.SECOND_BUTTON_IN_SKILLS_HUB, 1)

    def assert_text_from_skill_hub(self):
        assert not self.get_locator_by_contains_text(self.elements.TITLE_PYTHON).is_displayed()
        assert self.get_locator_by_contains_text(self.elements.TITLE_EXCEL).is_displayed()
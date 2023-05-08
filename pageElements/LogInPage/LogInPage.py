from Helper import Helper
from pageElements.LogInPage.LogInLocators import LogInLocators


class LogInPage(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = LogInLocators()

    def click_google_button(self):
        self.click_button(self.elements.GOOGLE_BUTTON)

    def switch_to_google(self):
        self.switch_to_new_window()

    def google_title(self):
        text = self.get_locator_by_xpath(self.elements.GOOGLE_TITLE).text
        assert text == "Вход"

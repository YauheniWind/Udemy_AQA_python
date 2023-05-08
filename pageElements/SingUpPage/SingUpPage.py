from Helper import Helper
from pageElements.SingUpPage.SingUpLocators import SingUpLocators


class SingUpPage(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = SingUpLocators()

    def click_sing_up(self):
        self.click_button(self.elements.SING_UP_BUTTON)

    def assert_registration_form(self):
        assert self.get_locator_by_xpath(self.elements.REGISTRATION_FORM)
        assert (
            self.current_url()
            == "https://www.udemy.com/join/signup-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fjoin%2Flogin-popup%2F%3Flocale%3Den_US%26response_type%3Dhtml%26next%3Dhttps%253A%252F%252Fwww.udemy.com%252F%253Fpersist_locale%253D%2526locale%253Den_US"
        )

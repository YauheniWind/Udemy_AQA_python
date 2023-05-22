from Helper import Helper
from pageObjects.locators.BusinessLocators import BusinessLocators


class BusinessPage(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = BusinessLocators()

    def none_element(self):
        self.display_none(self.elements.CONTAINER_COOKIE)

    def assert_logo_is_displayed(self):
        assert self.get_locator_by_xpath(self.elements.BUSINESS_LOGO)

    def click_on_logo(self):
        self.click_button(self.elements.BUSINESS_LOGO)

    def fill_form(self):
        self.send_keys(self.elements.WORK_EMAIL_INPUT, self.elements.EMAIL)
        self.send_keys(self.elements.FIRST_NAME_INPUT, self.elements.NAME)
        self.send_keys(self.elements.LAST_NAME_INPUT, self.elements.LAST_NAME)
        self.send_keys(self.elements.PHONE_NUMBER_INPUT, self.elements.PHONE_NUMBER)
        self.send_keys(self.elements.COMPANY_NAME_INPUT, self.elements.COMPANY_NAME)
        self.send_keys(self.elements.TITLE_INPUT, self.elements.JOB_TITLE)
        self.select_option(self.elements.COUNTRY_SELECT, self.elements.COUNTRY_NAME)

    def click_get_in_touch(self):
        self.click_button(self.elements.GET_IN_TOUCH_BUTTON)

    def assert_page(self):
        assert self.current_url() != 'https://business.udemy.com/request-demo-mx/?locale=en_US&mx_pg=httpcachecontextsme-list&ref=ufb_header&user_type=visitor&utm_type=mx'
import allure

from base_page import BasePage
from pageObjects.locators.teach_locators import TeachLocators


class TeachPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = TeachLocators()

    @allure.step("asserted main banner")
    def assert_find_main_banner(self):
        assert self.get_locator_by_xpath(self.elements.MAIN_BANNER)

    @allure.step("clicked 'get started'")
    def click_get_started(self):
        self.click_button(self.elements.GET_START_BUTTON)

    @allure.step("asserted modal window is displayed")
    def assert_modal_window_is_displayed(self):
        assert self.waiting_disappearance_element(self.elements.BECOME_INSTRUCTOR)

    @allure.step("scrolled to banner begin")
    def scroll_to_banner_begin(self):
        self.scroll_to_element(self.elements.HOW_TO_BEGIN)

    @allure.step("clicked video")
    def click_on_video(self):
        self.click_button(self.elements.SECOND_BUTTON)

    @allure.step("clicked course")
    def click_on_course(self):
        self.click_button(self.elements.SECOND_BUTTON, 1)

    @allure.step("asserted video is changer")
    def assert_banner_is_change_on_video(self):
        assert self.get_locator_by_xpath(self.elements.BANNER_INFO, 1)

    @allure.step("asserted course is change")
    def assert_banner_is_change_on_course(self):
        assert self.get_locator_by_xpath(self.elements.BANNER_INFO, 2)

    @allure.step("scrolled to comment from teacher")
    def scroll_to_comments_from_teacher(self):
        self.scroll_to_element(self.elements.COMMENTS_FROM_TEACHERS_BANNER)

    @allure.step("clicked next comment")
    def click_next_comment(self):
        self.click_button(self.elements.NEXT_COMMENT_BUTTON)

    @allure.step("asserted name of teacher")
    def assert_name_of_teachers(self):
        assert self.get_locator_by_xpath(self.elements.INFO_CART)

    @allure.step("displayed none element")
    def none_element(self):
        self.send_display_none(self.elements.CONTAINER_COOKIE)

    @allure.step("scrolled to support teacher")
    def scroll_to_support_teacher(self):
        self.scroll_to_element(self.elements.HELP_FOR_TEACHER)

    @allure.step("clicked support teacher")
    def click_support_teacher(self):
        self.click_button(self.elements.NEED_MORE_DETAILS_BUTTON)

    @allure.step("asserted window is switch to support teacher")
    def assert_switch_to_support_teacher_window(self):
        self.switch_to_new_window()
        assert self.current_url() != "https://www.udemy.com/teaching/?ref=teach_header"

    @allure.step("scrolled to 'get started' in footer")
    def scroll_to_get_started_footer(self):
        self.scroll_to_element(self.elements.FOOTER)

    @allure.step("clicked 'get started' in footer")
    def click_get_started_footer(self):
        self.click_button(self.elements.GET_STARTED_BUTTON_FOOTER)

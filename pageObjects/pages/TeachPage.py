from Helper import Helper
from pageObjects.locators.TeachLocators import TeachLocators


class TeachPage(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = TeachLocators()

    def delete_all_cookie(self):
        self.delete_all_cookies()

    def assert_find_main_banner(self):
        assert self.get_locator_by_xpath(self.elements.MAIN_BANNER)

    def click_get_started(self):
        self.click_button(self.elements.GET_START_BUTTON)

    def assert_modal_window_is_displayed(self):
        assert self.waiting_disappearance_element(self.elements.BECOME_INSTRUCTOR)

    def scroll_to_banner_begin(self):
        self.scroll_to_element(self.elements.HOW_TO_BEGIN)

    def click_on_video(self):
        self.click_button(self.elements.SECOND_BUTTON)

    def click_on_course(self):
        self.click_button(self.elements.SECOND_BUTTON, 1)

    def assert_banner_is_change_on_video(self):
        assert self.get_locator_by_xpath(self.elements.BANNER_INFO, 1)

    def assert_banner_is_change_on_course(self):
        assert self.get_locator_by_xpath(self.elements.BANNER_INFO, 2)

    def scroll_to_comments_from_teacher(self):
        self.scroll_to_element(self.elements.COMMENTS_FROM_TEACHERS_BANNER)

    def click_next_comment(self):
        self.click_button(self.elements.NEXT_COMMENT_BUTTON)

    def assert_name_of_teachers(self):
        assert self.get_locator_by_xpath(self.elements.INFO_CART)

    def none_element(self):
        self.display_none(self.elements.CONTAINER_COOKIE)

    def scroll_to_support_teacher(self):
        self.scroll_to_element(self.elements.HELP_FOR_TEACHER)

    def click_support_teacher(self):
        self.click_button(self.elements.NEED_MORE_DETAILS_BUTTON)

    def assert_switch_to_support_teacher_window(self):
        self.switch_to_new_window()
        assert self.current_url() != 'https://www.udemy.com/teaching/?ref=teach_header'

    def scroll_to_get_started_footer(self):
        self.scroll_to_element(self.elements.FOOTER)

    def click_get_started_footer(self):
        self.click_button(self.elements.GET_STARTED_BUTTON_FOOTER)

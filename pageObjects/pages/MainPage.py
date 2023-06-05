from Helper import Helper
from pageObjects.locators.MainLocators import MainLocators


class MainPage(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = MainLocators()

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

    def click_develop(self):
        self.mouse_moving(self.elements.CATEGORIES)
        self.mouse_click(self.elements.DEVELOPER_BUTTON, 0)

    def asser_change_main_page_url(self):
        assert self.current_url() != "https://www.udemy.com/"

    def enter_text_in_search(self):
        self.send_keys(self.elements.SEARCH_INPUT, "Python")

    def click_enter(self):
        self.keyboard_click(self.elements.SEARCH_INPUT)

    def assert_find_python_courses(self):
        assert self.current_url() == 'https://www.udemy.com/courses/search/?src=ukw&q=Python'

    def select_business(self):
        self.mouse_moving(self.elements.UDEMY_BUSINESS)

    def assert_business_modal_window(self):
        assert self.get_element_by_xpath(self.elements.BUSINESS_MODAL_WINDOW).is_displayed()

    def click_try_business(self):
        self.mouse_click(self.elements.TRY_UDEMY_BUSINESS)

    def select_teach(self):
        self.mouse_moving(self.elements.TEACH_ON_UDEMY)

    def assert_teach_modal_window(self):
        element = self.get_locator_by_xpath(self.elements.TEACH_MODAL_WINDOW, 1)
        if element:
            assert True

    def click_learn_more(self):
        self.click_button(self.elements.LEARN_MORE)

    def display_teach(self):
        self.display_block(self.elements.BLOCK_TEACH)

    def choose_language_button(self):
        self.click_button(self.elements.CHOOSE_A_LANGUAGE)

    def choose_language_russian(self):
        self.click_button(self.elements.RUSSIAN_LANGUAGE)

    def assert_title_change_language(self):
        assert self.get_locator_by_xpath(self.elements.CHANGED_LANGUAGE_BANNER).text == self.elements.TITLE_IN_RUSSIAN

    def select_basket(self):
        self.mouse_moving(self.elements.BASKET_CART)

    def assert_title_in_basket(self):
        assert self.get_inner_text(self.elements.BASKET_MODAL_WINDOW) == self.elements.BASKET_EMPTY_TITLE

    def add_product_in_basket(self):
        self.click_button(self.elements.ADD_TO_BASKET)

    def click_close_pop_up(self):
        self.click_button(self.elements.CLOSE_POP_UP)

    def assert_product_in_basket(self):
        assert self.get_inner_text(self.elements.PRODUCT_INFO_IN_BASKET) == self.elements.NAME_OF_PRODUCT

    def assert_banner_above_header(self):
        assert self.get_locator_by_xpath(self.elements.BANNER_ABOVE_HEADER)

    def close_banner_above_header(self):
        self.click_button(self.elements.CLOSE_BANNER_ABOVE_HEADER)

    def assert_not_banner_above_header(self):
        assert self.waiting_disappearance_element(self.elements.BANNER_ABOVE_HEADER)

    def click_log_in(self):
        self.click_button(self.elements.LOG_IN)

    def click_sing_up(self):
        self.click_button(self.elements.SIGN_UP)

    # Body

    def assert_general_banner_main_page(self):
        assert self.get_locator_by_xpath(self.elements.GENERAL_BANNER)

    def click_yes(self):
        self.click_button(self.elements.PRIVACY)

    def click_accept(self):
        self.click_button(self.elements.ACCEPT_PRIVACY)

    def scroll_to_skill_hub(self):
        self.scroll_to_element(self.elements.SKILLS_HUB)

    def click_on_second_button(self):
        self.click_button(self.elements.SECOND_BUTTON_IN_SKILLS_HUB, 1)

    def assert_text_from_skill_hub(self):
        assert not self.get_locator_by_contains_text(
            self.elements.TITLE_PYTHON
        ).is_displayed()
        assert self.get_locator_by_contains_text(
            self.elements.TITLE_EXCEL
        ).is_displayed()

    def click_explore_python(self):
        self.get_locator_by_contains_text('Explore Python')

    def scroll_to_explore(self):
        self.scroll_to_element(self.elements.HOW_LEARN_TITLE)

    def next_banner(self):
        self.click_button(self.elements.ARROW_NEXT)

    def assert_cart_of_product(self):
        assert self.get_element_by_xpath(self.elements.CART)

    def select_product(self):
        self.mouse_moving(self.elements.CART_ON_MAIN_PAGE)

    def assert_info_cart(self):
        assert self.get_locator_by_xpath(self.elements.TITLE_MODAL_WINDOW_CART)

    def click_add_to_cart(self):
        self.mouse_moving(self.elements.CART_ON_MAIN_PAGE)
        self.click_button(self.elements.ADD_TO_CART_BUTTON)

    def click_add_to_wish_list(self):
        self.mouse_moving(self.elements.CART_ON_MAIN_PAGE)
        self.click_button(self.elements.ADD_TO_WISH_LIST_BUTTON)

    def assert_how_to_learn_section(self):
        assert self.get_locator_by_xpath(self.elements.HOW_LEARN_SECTION)

    def scroll_to_students(self):
        self.scroll_to_element(self.elements.STUDENTS)

    def click_next_button_section_how_learn(self):
        self.click_button(self.elements.NEXT_BUTTON_HOW_LEARN)

    def assert_student_name_is_change(self):
        assert self.get_inner_text(self.elements.STUDENTS_NAME, 3) == 'Surya M'

    def assert_info_in_cart_of_comment(self):
        assert self.get_locator_by_xpath(self.elements.COMMENT_IN_HOW_LEARN).is_displayed()
        assert self.get_locator_by_xpath(self.elements.NAME_OF_COURSE_IN_HOW_LEARN).is_displayed()
        assert self.get_locator_by_xpath(self.elements.STUDENTS_NAME).is_displayed()

    def click_course(self):
        self.click_button(self.elements.NAME_OF_COURSE_IN_HOW_LEARN)

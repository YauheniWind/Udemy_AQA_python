import allure

from base_page import BasePage
from pageObjects.locators.main_locators import MainLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = MainLocators()

    # Header
    @allure.step("fined logo")
    def find_element_logo(self):
        assert self.get_locator_by_xpath(self.elements.LOGO)

    @allure.step("clicked on logo")
    def click_on_logo(self):
        self.click_button(self.elements.LOGO)

    @allure.step("checked url address")
    def check_url(self):
        assert self.current_url() == "https://www.udemy.com/"

    @allure.step("fined logo")
    def find_categories(self):
        self.get_locator_by_xpath(self.elements.CATEGORIES)

    @allure.step("moved mouse on categories")
    def mouse_moving_to_categories(self):
        self.mouse_moving(self.elements.CATEGORIES)

    @allure.step("asserted find subcategories")
    def assert_find_element_sub_categories(self):
        assert self.get_locator_by_xpath(self.elements.SUB_CATEGORIES)

    @allure.step("clicked develop button")
    def click_develop(self):
        self.mouse_moving(self.elements.CATEGORIES)
        self.mouse_click(self.elements.DEVELOPER_BUTTON, 0)

    @allure.step("asserted main page is change")
    def asser_change_main_page_url(self):
        assert self.current_url() != "https://www.udemy.com/"

    @allure.step("entered text")
    def enter_text_in_search(self):
        self.send_keys(self.elements.SEARCH_INPUT, "Python")

    @allure.step("clicked 'Enter' on keyboard")
    def click_enter(self):
        self.keyboard_click(self.elements.SEARCH_INPUT)

    @allure.step("asserted find courses")
    def assert_find_python_courses(self):
        assert self.current_url() != "https://www.udemy.com/"

    @allure.step("selected business with mouse")
    def select_business(self):
        self.mouse_moving(self.elements.UDEMY_BUSINESS)

    @allure.step("asserted business modal window is displayed")
    def assert_business_modal_window(self):
        assert self.get_element_by_xpath(
            self.elements.BUSINESS_MODAL_WINDOW
        ).is_displayed()

    @allure.step("clicked 'Try business'")
    def click_try_business(self):
        self.mouse_click(self.elements.TRY_UDEMY_BUSINESS)

    @allure.step("selected teach on udemy")
    def select_teach(self):
        self.mouse_moving(self.elements.TEACH_ON_UDEMY)

    @allure.step("asserted tech modal window is displayed")
    def assert_teach_modal_window(self):
        element = self.get_locator_by_xpath(self.elements.TEACH_MODAL_WINDOW, 1)
        if element:
            assert True

    @allure.step("clicked 'Learn more'")
    def click_learn_more(self):
        self.click_button(self.elements.LEARN_MORE)

    @allure.step("clicked language button")
    def choose_language_button(self):
        self.click_button(self.elements.CHOOSE_A_LANGUAGE)

    @allure.step("selected russian language")
    def choose_language_russian(self):
        self.click_button(self.elements.RUSSIAN_LANGUAGE)

    @allure.step("asserted language was change")
    def assert_title_change_language(self):
        assert self.current_url()

    @allure.step("selected basket")
    def select_basket(self):
        self.mouse_moving(self.elements.BASKET_CART)

    @allure.step("asserted basket title")
    def assert_title_in_basket(self):
        assert (
            self.get_inner_text(self.elements.BASKET_MODAL_WINDOW)
            == self.elements.BASKET_EMPTY_TITLE
        )

    @allure.step("added product to basket")
    def add_product_in_basket(self):
        self.click_button(self.elements.ADD_TO_BASKET)

    @allure.step("closed pop up window")
    def click_close_pop_up(self):
        self.click_button(self.elements.CLOSE_POP_UP)

    @allure.step("asserted product in basket")
    def assert_product_in_basket(self):
        assert (
            self.get_inner_text(self.elements.PRODUCT_INFO_IN_BASKET)
            == self.elements.NAME_OF_PRODUCT
        )

    @allure.step("asserted banner above header")
    def assert_banner_above_header(self):
        assert self.get_locator_by_xpath(self.elements.BANNER_ABOVE_HEADER)

    @allure.step("closed banner above header")
    def close_banner_above_header(self):
        self.click_button(self.elements.CLOSE_BANNER_ABOVE_HEADER)

    @allure.step("asserted banner above header is close")
    def assert_not_banner_above_header(self):
        assert self.waiting_disappearance_element(self.elements.BANNER_ABOVE_HEADER)

    @allure.step("clicked button log in")
    def click_log_in(self):
        self.click_button(self.elements.LOG_IN)

    @allure.step("clicked button sing up")
    def click_sing_up(self):
        self.click_button(self.elements.SIGN_UP)

    # Body
    @allure.step("asserted general banner is displayed")
    def assert_general_banner_main_page(self):
        assert self.get_locator_by_xpath(self.elements.GENERAL_BANNER)

    @allure.step("clicked 'yes' in privacy banner")
    def click_yes(self):
        self.click_button(self.elements.PRIVACY)

    @allure.step("clicked 'accept' in privacy banner")
    def click_accept(self):
        self.click_button(self.elements.ACCEPT_PRIVACY)

    @allure.step("scrolled to skill hub")
    def scroll_to_skill_hub(self):
        self.scroll_to_element(self.elements.SKILLS_HUB)

    @allure.step("clicked second option in skill hub")
    def click_on_second_button(self):
        self.click_button(self.elements.SECOND_BUTTON_IN_SKILLS_HUB, 1)

    @allure.step("asserted text")
    def assert_text_from_skill_hub(self):
        assert not self.get_locator_by_contains_text(
            self.elements.TITLE_PYTHON
        ).is_displayed()
        assert self.get_locator_by_contains_text(
            self.elements.TITLE_EXCEL
        ).is_displayed()

    @allure.step("clicked explore python")
    def click_explore_python(self):
        self.get_locator_by_contains_text("Explore Python")

    @allure.step("scrolled to explore")
    def scroll_to_explore(self):
        self.scroll_to_element(self.elements.HOW_LEARN_TITLE)

    @allure.step("changed banner")
    def next_banner(self):
        self.click_button(self.elements.ARROW_NEXT)

    @allure.step("asserted cart of product")
    def assert_cart_of_product(self):
        assert self.get_element_by_xpath(self.elements.CART)

    @allure.step("selected product")
    def select_product(self):
        self.mouse_moving(self.elements.CART_ON_MAIN_PAGE)

    @allure.step("asserted info about product")
    def assert_info_cart(self):
        assert self.get_locator_by_xpath(self.elements.TITLE_MODAL_WINDOW_CART)

    @allure.step("clicked add to cart")
    def click_add_to_cart(self):
        self.mouse_moving(self.elements.CART_ON_MAIN_PAGE)
        self.click_button(self.elements.ADD_TO_CART_BUTTON)

    @allure.step("clicked add to wish list")
    def click_add_to_wish_list(self):
        self.mouse_moving(self.elements.CART_ON_MAIN_PAGE)
        self.click_button(self.elements.ADD_TO_WISH_LIST_BUTTON)

    @allure.step("asserted 'how to learn' section is displayed")
    def assert_how_to_learn_section(self):
        assert self.get_locator_by_xpath(self.elements.HOW_LEARN_SECTION)

    @allure.step("scrolled to students section")
    def scroll_to_students(self):
        self.scroll_to_element(self.elements.STUDENTS)

    @allure.step("clicked button next")
    def click_next_button_section_how_learn(self):
        self.click_button(self.elements.NEXT_BUTTON_HOW_LEARN)

    @allure.step("asserted student name was change")
    def assert_student_name_is_change(self):
        assert self.get_inner_text(self.elements.STUDENTS_NAME, 3) == "Surya M"

    @allure.step("asserted info in comment cart is displayed")
    def assert_info_in_cart_of_comment(self):
        assert self.get_locator_by_xpath(
            self.elements.COMMENT_IN_HOW_LEARN
        ).is_displayed()
        assert self.get_locator_by_xpath(
            self.elements.NAME_OF_COURSE_IN_HOW_LEARN
        ).is_displayed()
        assert self.get_locator_by_xpath(self.elements.STUDENTS_NAME).is_displayed()

    @allure.step("clicked on course")
    def click_course(self):
        self.click_button(self.elements.NAME_OF_COURSE_IN_HOW_LEARN)

    @allure.step("clicked 'show more' button")
    def click_show_more(self):
        self.click_button(self.elements.SHOW_MORE_BUTTON, 0)

    @allure.step("clicked russian check box")
    def click_russian(self):
        self.click_button(self.elements.RUSSIAN_CHECK_BOX, 13)

    @allure.step("asserted result label")
    def assert_label_result(self):
        assert self.waiting_disappearance_element(self.elements.LABEL_RESULT)

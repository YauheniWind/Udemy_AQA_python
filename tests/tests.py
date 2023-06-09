import time

from pageObjects.pages.LogInPage import LogInPage
from pageObjects.pages.MainPage import MainPage
from pageObjects.pages.BusinessPage import BusinessPage
from pageObjects.pages.SingUpPage import SingUpPage
from pageObjects.pages.TeachPage import TeachPage
from pageObjects.pages.CartPage import CartPage


class TestMainPage:
    # ---------- HEADER -------------
    def test_logo(self, browser, open_main_page):
        logo_test = MainPage(browser)

        logo_test.find_element_logo()
        logo_test.click_on_logo()
        logo_test.check_url()

    def test_categories(self, browser, open_main_page):
        categories_test = MainPage(browser)

        categories_test.find_categories()
        categories_test.mouse_moving_to_categories()
        categories_test.find_element_sub_categories()

    def test_choose_developer_from_categories(self, browser, open_main_page):
        choose_developer = MainPage(browser)

        choose_developer.find_categories()
        choose_developer.click_develop()
        choose_developer.asser_change_main_page_url()

    def test_search(self, browser, open_main_page):
        search = MainPage(browser)

        search.enter_text_in_search()
        search.click_enter()
        search.assert_find_python_courses()

    def test_business_modal_window(self, browser, open_main_page):
        business_modal_window = MainPage(browser)

        business_modal_window.select_business()
        business_modal_window.assert_business_modal_window()

    def test_click_try_udemy_business(self, browser, open_main_page):
        try_udemy_business = MainPage(browser)

        try_udemy_business.select_business()
        try_udemy_business.click_try_business()
        try_udemy_business.asser_change_main_page_url()

    def test_tech_modal_window(self, browser, open_main_page):
        teach_modal_window = MainPage(browser)

        teach_modal_window.select_teach()
        teach_modal_window.assert_teach_modal_window()

    def test_click_learn_more(self, browser, open_main_page):
        learn_more = MainPage(browser)

        learn_more.select_teach()
        learn_more.click_learn_more()
        learn_more.asser_change_main_page_url()

    def test_change_language(self, browser, open_main_page):
        change_language = MainPage(browser)

        change_language.choose_language_button()
        change_language.choose_language_russian()
        change_language.assert_title_change_language()

    def test_basket_modal_window(self, browser, open_main_page):
        basket_modal_window = MainPage(browser)

        basket_modal_window.select_basket()
        basket_modal_window.assert_title_in_basket()

    def test_add_to_basket(self, browser, open_page):
        add_to_basket = MainPage(browser)

        add_to_basket.add_product_in_basket()
        add_to_basket.select_basket()
        add_to_basket.click_close_pop_up()
        add_to_basket.assert_product_in_basket()

    def test_banner_above_header(self, browser, open_main_page):
        banner_above_header = MainPage(browser)

        banner_above_header.assert_banner_above_header()
        banner_above_header.close_banner_above_header()
        banner_above_header.assert_not_banner_above_header()

    def test_click_log_in(self, browser, open_main_page):
        click_log_in = MainPage(browser)

        click_log_in.click_log_in()
        click_log_in.asser_change_main_page_url()

    def test_click_sing_up(self, browser, open_main_page):
        click_sing_up = MainPage(browser)

        click_sing_up.click_sing_up()
        click_sing_up.asser_change_main_page_url()

    # ---------- BODY -------------

    def test_general_banner(self, browser, open_main_page):
        main_banner = MainPage(browser)

        main_banner.assert_general_banner_main_page()

    def test_skill_hub(self, browser, open_main_page):
        skill_hub = MainPage(browser)

        skill_hub.click_yes()
        skill_hub.click_accept()

        skill_hub.scroll_to_skill_hub()

        skill_hub.click_on_second_button()

        skill_hub.assert_text_from_skill_hub()

    def test_explore_python(self, browser, open_main_page):
        explore_python = MainPage(browser)

        explore_python.click_yes()
        explore_python.click_accept()
        explore_python.scroll_to_explore()
        explore_python.click_explore_python()
        explore_python.asser_change_main_page_url()

    def test_scroll_courses(self, browser, open_main_page):
        scroll_courses = MainPage(browser)

        scroll_courses.click_yes()
        scroll_courses.click_accept()
        scroll_courses.scroll_to_explore()
        scroll_courses.next_banner()
        scroll_courses.assert_cart_of_product()

    def test_cart_modal_window(self, browser, open_main_page):
        cart_modal_window = MainPage(browser)

        cart_modal_window.scroll_to_explore()
        cart_modal_window.select_product()
        cart_modal_window.assert_info_cart()

    def test_add_product_to_basket(self, browser, open_main_page):
        add_product_to_basket = MainPage(browser)

        add_product_to_basket.scroll_to_explore()
        add_product_to_basket.click_add_to_cart()
        add_product_to_basket.select_basket()
        add_product_to_basket.assert_title_in_basket()

    def test_add_to_wish_list(self, browser, open_main_page):
        add_to_wish_list = MainPage(browser)

        add_to_wish_list.scroll_to_explore()
        add_to_wish_list.click_add_to_wish_list()
        add_to_wish_list.asser_change_main_page_url()

    def test_how_to_learn_section(self, browser, open_main_page):
        how_to_learn_section = MainPage(browser)

        how_to_learn_section.scroll_to_students()
        how_to_learn_section.assert_how_to_learn_section()

    def test_scroll_to_learn_section(self, browser, open_main_page):
        how_to_learn_section = MainPage(browser)

        how_to_learn_section.scroll_to_students()
        how_to_learn_section.click_next_button_section_how_learn()
        how_to_learn_section.assert_student_name_is_change()

    def test_info_how_learn(self, browser, open_main_page):
        info_how_learn = MainPage(browser)

        info_how_learn.scroll_to_students()
        info_how_learn.assert_info_in_cart_of_comment()

    def test_select_course(self, browser, open_main_page):
        select_course = MainPage(browser)

        select_course.scroll_to_students()
        select_course.click_course()
        select_course.asser_change_main_page_url()

    def test_search_filter(self, browser, open_search_result):
        search_filter = MainPage(browser)

        search_filter.click_show_more()
        search_filter.click_russian()
        search_filter.assert_label_result()


class TestBusinessPage:
    def test_logo(self, browser, open_business_page):
        logo_test = BusinessPage(browser)

        logo_test.assert_logo_is_displayed()
        logo_test.click_on_logo()

    def test_send_form(self, browser, open_business_page):
        send_form = BusinessPage(browser)

        send_form.none_element()
        send_form.fill_form()
        send_form.click_get_in_touch()
        browser.refresh()
        send_form.assert_page()


class TestTeachPage:
    def test_main_banner(self, browser, open_teach_page):
        banner_test = TeachPage(browser)

        banner_test.none_element()
        banner_test.assert_find_main_banner()
        banner_test.click_get_started()
        banner_test.assert_modal_window_is_displayed()

    def test_how_to_begin(self, browser, open_teach_page):
        banner_test = TeachPage(browser)

        banner_test.none_element()
        banner_test.scroll_to_banner_begin()
        banner_test.click_on_video()
        banner_test.assert_banner_is_change_on_video()
        banner_test.click_on_course()
        banner_test.assert_banner_is_change_on_course()

    def test_teachers_comments(self, browser, open_teach_page):
        teachers_comments = TeachPage(browser)

        teachers_comments.none_element()
        teachers_comments.scroll_to_comments_from_teacher()
        teachers_comments.click_next_comment()
        teachers_comments.assert_name_of_teachers()

    def test_support_teacher(self, browser, open_teach_page):
        support_teacher = TeachPage(browser)

        support_teacher.none_element()
        support_teacher.scroll_to_support_teacher()
        support_teacher.click_support_teacher()
        support_teacher.assert_switch_to_support_teacher_window()

    def test_get_started_footer(self, browser, open_teach_page):
        get_started_footer = TeachPage(browser)

        get_started_footer.none_element()
        get_started_footer.scroll_to_get_started_footer()
        get_started_footer.click_get_started_footer()
        get_started_footer.assert_modal_window_is_displayed()


class TestLogIn:
    def test_google_button(self, browser, open_log_in_page):
        google_button = LogInPage(browser)

        google_button.click_google_button()
        google_button.switch_to_google()
        google_button.assert_google_title()

    def test_facebook_button(self, browser, open_log_in_page):
        facebook_button = LogInPage(browser)

        facebook_button.click_facebook_button()
        facebook_button.assert_facebook_page()

    def test_apple_button(self, browser, open_log_in_page):
        apple_button = LogInPage(browser)

        apple_button.click_apple_button()
        apple_button.assert_apple_title()

    def test_log_in_button(self, browser, open_log_in_page):
        log_in_button = LogInPage(browser)

        log_in_button.click_log_in()
        log_in_button.assert_page_not_change()


class TestSingUp:
    def test_sing_up_empty(self, browser, open_sing_up_page):
        sing_up = SingUpPage(browser)

        sing_up.click_sing_up()
        sing_up.assert_registration_form()

    def test_sign_up(self, browser, open_sing_up_page):
        sing_up = SingUpPage(browser)

        sing_up.fill_registration_form()
        sing_up.click_sing_up()
        sing_up.assert_change_page()


class TestCart:
    def test_buy_now(self, browser, open_cart_page):
        buy_now = CartPage(browser)

        buy_now.click_buy_now()
        buy_now.check_url()

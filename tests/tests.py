import time

from pageObjects.pages.LogInPage import LogInPage
from pageObjects.pages.MainPage import MainPage
from pageObjects.pages.BusinessPage import BusinessPage
from pageObjects.pages.SingUpPage import SingUpPage
from pageObjects.pages.TeachPage import TeachPage


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
        choose_developer.mouse_moving_to_categories()
        choose_developer.click_develop()
        choose_developer.asser_change_main_page_url()

    def test_search(self, browser, open_main_page):
        search = MainPage(browser)

        search.enter_text_in_search()
        search.click_enter()
        search.assert_find_python_courses()
        time.sleep(5)

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

    # ---------- BODY -------------
    def test_skill_hub(self, browser, open_main_page):
        skill_hub = MainPage(browser)

        skill_hub.click_yes()
        skill_hub.click_accept()

        skill_hub.scroll_to_skill_hub()

        skill_hub.click_on_second_button()

        skill_hub.assert_text_from_skill_hub()


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

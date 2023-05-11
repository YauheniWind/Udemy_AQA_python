import time

from pageObjects.pages.LogInPage import LogInPage
from pageObjects.pages.MainPage import MainPage
from pageObjects.pages.BusinessPage import BusinessPage
from pageObjects.pages.SingUpPage import SingUpPage
from pageObjects.pages.TeachPage import TeachPage


class TestMainPage:
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


class TestTeachPage:
    def test_main_banner(self, browser, open_teach_page):
        banner_test = TeachPage(browser)

        banner_test.assert_find_main_banner()
        banner_test.click_get_started()
        banner_test.assert_modal_window_is_displayed()

    def test_how_to_begin(self, browser, open_teach_page):
        banner_test = TeachPage(browser)

        banner_test.scroll_to_banner_begin()
        banner_test.click_on_video()
        banner_test.assert_banner_is_change_on_video()
        banner_test.click_on_course()
        banner_test.assert_banner_is_change_on_course()


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

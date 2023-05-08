from pageElements.LogInPage.LogInPage import LogInPage
from pageElements.MainPage.MainPage import MainPage
from pageElements.BusinessPage.BusinessPage import BusinessPage
from pageElements.SingUpPage.SingUpPage import SingUpPage
from pageElements.TeachPage.TeachPage import TeachPage


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


class TestLogIn:
    def test_google_button(self, browser, open_log_in_page):
        google_button = LogInPage(browser)

        google_button.click_google_button()
        google_button.switch_to_google()
        google_button.google_title()


class TestSingUp:
    def test_sing_up_empty(self, browser, open_sing_up_page):
        sing_up = SingUpPage(browser)

        sing_up.click_sing_up()
        sing_up.assert_registration_form()

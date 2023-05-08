from pageElements.MainPage.MainPage import MainPage


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

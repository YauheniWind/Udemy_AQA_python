from pageElements.HeaderPage import HeaderPage


def test_logo(browser, open_main_page):
    logo_test = HeaderPage(browser)

    logo_test.waiting_logo()
    logo_test.find_element()
    logo_test.click_on_logo()
    logo_test.current_url()

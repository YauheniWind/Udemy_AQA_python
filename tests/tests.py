from pageElements.HeaderPage import HeaderPage


def test_logo(browser, open_main_page):
    logo_test = HeaderPage(browser)


    logo_test.find_element_logo()
    logo_test.click_on_logo()
    logo_test.check_url()

def test_categories(browser, open_main_page):
    categories_test = HeaderPage(browser)

    categories_test.find_categories()
    categories_test.mouse_moving_to_categories()
    categories_test.find_element_sub_categories()
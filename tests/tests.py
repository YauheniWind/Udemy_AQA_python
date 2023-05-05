from pageElements.Header import Header

def test_logo(browser, open_main_page):
    logo_test = Header(browser)

    logo_test.waiting_logo()
    logo_test.click_on_logo()
    logo_test.current_url()
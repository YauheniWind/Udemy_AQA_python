import pytest
import time
import os

from allure_commons import fixture
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

from datetime import datetime
from selenium import webdriver as selenium_webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def browser():
    driver = webdriver.Chrome(
        ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
    )
    driver.implicitly_wait(1)

    yield driver

    driver.close()
    driver.quit()


def browser_make(request):
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome(options=options)
        driver.implicitly_wait(5)
    else:
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)

    yield driver

    driver.close()
    driver.quit()


@pytest.fixture()
def browser_firefox():
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.implicitly_wait(1)

    yield driver

    driver.close()
    driver.quit()


@pytest.fixture()
def credentials():
    return {"login": "standard_user", "password": "secret_sauce"}


def pytest_addoption(parser):
    parser.addoption(
        "--address",
        action="store",
        default="http://192.168.122.244/",
        help="HuntBox web address",
    )
    parser.addoption(
        "--browser", action="store", default="firefox", help="Browser name"
    )


@pytest.fixture
def open_page(browser):
    browser.get("https://www.udemy.com/course/complete-python-bootcamp/?persist_locale=&locale=en_US")
    browser.fullscreen_window()


@pytest.fixture
def open_main_page(browser):
    browser.get("https://www.udemy.com/?persist_locale=&locale=en_US")
    browser.fullscreen_window()


@pytest.fixture
def open_business_page(browser):
    browser.get(
        "https://business.udemy.com/request-demo-mx/?locale=en_US&mx_pg=httpcachecontextsme-list&ref=ufb_header&user_type=visitor&utm_type=mx"
    )
    browser.fullscreen_window()


@pytest.fixture
def open_teach_page(browser):
    browser.get("https://www.udemy.com/teaching/?persist_locale=&locale=en_US")
    browser.fullscreen_window()


@pytest.fixture()
def open_log_in_page(browser):
    browser.get(
        'https://www.udemy.com/join/login-popup/?persist_locale=&locale=en_US'
    )
    browser.maximize_window()


@pytest.fixture()
def open_sing_up_page(browser):
    browser.get(
        "https://www.udemy.com/join/signup-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fjoin%2Flogin-popup%2F%3Flocale%3Den_US%26response_type%3Dhtml%26next%3Dhttps%253A%252F%252Fwww.udemy.com%252F%253Fpersist_locale%253D%2526locale%253Den_US"
    )
    browser.maximize_window()


# set up a hook to be able to check if a test has failed
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     # execute all other hooks to obtain the report object
#     outcome = yield
#     rep = outcome.get_result()
#
#     # set a report attribute for each phase of a call, which can
#     # be "setup", "call", "teardown"
#
#     setattr(item, "rep_" + rep.when, rep)
#
# @pytest.hookimpl(tryfirst=True, hookwrapper=True)
# def pytest_runtest_makereport(item, call):
#     report = (yield).get_result()
#     if report.when == "call":
#         setattr(item, "report", report)
#
# # check if a test has failed
# @pytest.fixture(scope='function', autouse=True)
# def make_failed_screenshot(request):
#     yield
#     if request.node.report:  # See pytest_runtest_makereport() in conftest.py
#         if request.node.report.failed:
#             # TODO: refactor the next string to use path from the config: request.config.conf.pytest.screenshots
#             browser = webdriver.Chrome
#             path = 'p3_failed_tests_data/'
#             make_dir(path)
#             file_path = 'p3_failed_tests_data/' + f'{request.node.name}.png'
#             file_name = path + f'{request.node.name}.png'
#             browser.save_screenshot("/tests")
#             print('\nError path ', browser.current_url)
#             print('\nScreenshot ', file_path)
#
#
# # make a screenshot with a name of the test, date and time
# def take_screenshot(driver, nodeid):
#     time.sleep(1)
#     file_name = f'MY_{datetime.today().strftime("%Y-%m-%d_%H:%M")}.png'.replace(
#         "/", "_"
#     ).replace("::", "__")
#     print(file_name)
#     driver.save_screenshot(file_name)
#
#
# def make_dir(directory_name):
#     if not os.path.exists(directory_name):
#         os.makedirs(directory_name)

import pytest

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
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
    browser.get("http://the-internet.herokuapp.com/dynamic_controls")


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
        "https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2F%3Fpersist_locale%3D%26locale%3Den_US"
    )
    browser.maximize_window()


@pytest.fixture()
def open_sing_up_page(browser):
    browser.get(
        "https://www.udemy.com/join/signup-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Fjoin%2Flogin-popup%2F%3Flocale%3Den_US%26response_type%3Dhtml%26next%3Dhttps%253A%252F%252Fwww.udemy.com%252F%253Fpersist_locale%253D%2526locale%253Den_US"
    )
    browser.maximize_window()

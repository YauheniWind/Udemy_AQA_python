from Helper import Helper
from pageObjects.HeaderObject import HeaderObject


class HeaderPage(Helper):
    def __init__(self, driver):
        super().__init__(driver)

        self.elements = HeaderObject()

    def waiting_logo(self):
        """
        Метод ожидает элемент
        """
        self.waiting_element(self.elements.LOGO)

    def find_element_logo(self):
        """
        Метод находит елемент
        """
        assert self.get_locator_by_xpath(self.elements.LOGO)

    def click_on_logo(self):
        """
        Метод кликает на элемент
        """
        self.click_button(self.elements.LOGO)

    def url(self):
        """
        Метод сравнивает url адресс
        """
        assert self.current_url() == 'https://www.udemy.com/?persist_locale=&locale=en_US'

    def waiting_categories(self):
        """
        Метод ожидает элемент
        """
        self.waiting_element(self.elements.CATEGORIES)

    def mouse_moving_to_categories(self):
        """
        Метод для передвежения мыши
        """
        self.mouse_moving(HeaderObject.CATEGORIES)

    def find_element_sub_categories(self):
        """
        Метод ожидания сабкатегорий
        """
        assert self.get_locator_by_xpath(HeaderObject.SUB_CATEGORIES)
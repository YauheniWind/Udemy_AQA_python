from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


class Helper:
    def __init__(self, driver):
        self.driver = driver

    def get_locator_by_xpath(self, selector, index=0):
        # '//*[@id="userName"]'
        xpath = (By.XPATH, selector)
        elements = self.driver.find_elements(*xpath)
        return elements[index]

    def get_element_by_xpath(self, selector):
        return self.driver.find_element(By.XPATH, selector)

    def get_locator_by_css(self, selector):
        # .class_name
        css = (By.CSS_SELECTOR, selector)
        return self.driver.find_element(*css)

    def get_locator_by_id(self, selector):
        id = (By.ID, selector)
        return self.driver.find_element(*id)

    def get_locator_by_class_name(self, selector):
        # class_name
        class_name = (By.CLASS_NAME, selector)
        return self.driver.find_element(*class_name)

    def get_locator_by_contains(self, selector):
        xpath = (By.XPATH, f'//*[contains(@class,"{selector}")]')
        return self.driver.find_element(*xpath)

    def get_locator_by_contains_text(self, text):
        xpath = (By.XPATH, f'//*[contains(text(),"{text}")]')
        return self.driver.find_element(*xpath)

    def click_element(self, locator):
        self.driver.execute_script("arguments[0].scrollIntoView", locator)
        locator.click()

    def assert_that_element_is_selected(self, selector):
        return self.get_locator_by_css(selector).is_selected()

    def scroll_to_element(self, locator):
        iframe = self.get_locator_by_xpath(locator)
        ActionChains(self.driver).scroll_to_element(iframe).perform()
        # return ActionChains(self.driver).scroll_to_element(locator).perform()

    def scroll_to_element_offset(self, locator, scroll_offset):
        actions = ActionChains(self.driver)
        actions.move_to_element(locator).perform()
        return self.driver.execute_script(f"window.scrollBy(0, {scroll_offset});")

    def remove_element_from_DOM(self, locator):
        return self.driver.execute_script("arguments[0].remove();", locator)

    def select_value_from_dropdown(self, value):
        element = self.get_locator_by_xpath(value)
        element.click()

    def select_checkbox(self, locator, value=True):
        element = self.get_locator_by_xpath(locator)
        current_check = element.is_selected()
        if current_check != value:
            element.click()

    def click_button(self, locator, index=0):
        element = self.get_locator_by_xpath(locator, index)
        element.click()

    def switch_to_iframe(self, locator):
        return self.driver.switch_to.frame(self.driver.find_element(By.XPATH, locator))

    def get_element_text(self, locator):
        element = self.driver.find_element(*locator)
        return element.text

    def enter_text_and_get_attribute_value(self, locator, text):
        element = self.get_locator_by_xpath(locator)
        element.send_keys(text)
        entered_text = element.get_attribute("value")

        return entered_text

    def get_attribute_(self, locator, value):
        element = self.get_locator_by_xpath(locator)
        if value == "class":
            return element.get_attribute("class")
        elif value == "placeholder":
            return element.get_attribute("placeholder")
        else:
            return element.get_attribute("value")

    def waiting_element(self, locator):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, locator))
        )

    def waiting_disappearance_element(self, locator):
        return WebDriverWait(self.driver, 10).until_not(
            EC.presence_of_element_located((By.XPATH, locator))
        )

    def element_is_enabled(self, locator):
        element = self.get_locator_by_xpath(locator)
        if element.is_enabled():
            return True
        return False

    def ec_text_to_be_present_in_element(self, element, text):
        return EC.text_to_be_present_in_element(element, text)

    def current_url(self):
        return self.driver.current_url

    def mouse_moving(self, locator):
        element = self.waiting_element(locator)
        action = ActionChains(self.driver)
        return action.move_to_element(element).perform()

    def element_is_displayed(self, locator):
        element = self.get_locator_by_xpath(locator)
        if element.is_displayed():
            return True
        return False

    def delete_all_cookies(self):
        self.driver.delete_all_cookies()

    def switch_to_new_window(self):
        original_window = self.driver.current_window_handle
        new_window = [
            window for window in self.driver.window_handles if window != original_window
        ][0]
        return self.driver.switch_to.window(new_window)

    def alert_text(self):
        return Alert(self.driver).text

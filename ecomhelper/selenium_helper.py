from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


class Seleniumhelper:

    def __init__(self, driver):
        self.driver = driver

    def webelement_is_present(self, locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

        except TimeoutException:
            return 'Unable to find Locator'

    def webelement_enter(self, locator, text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(locator))
            element.clear()
            element.send_keys(text)
        except (TimeoutException, NoSuchElementException):
            print(f"Element with locator '{locator}' not found.")
            return None

    def webelement_click(self, locator):
        try:
            return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()
        except (TimeoutException, NoSuchElementException):
            print(f"Element with locator '{locator}' not found.")
            return None

    def webelement_text_content(self, locator, expected_content=None):
        try:
            content = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text
            assert content == expected_content, f"Content missmatch! Expected: {expected_content}, Found: '{content}'"
            # return print(f"Content = {content}")
        except (TimeoutException, NoSuchElementException):
            print(f"Element with locator '{locator}' not found.")
            return None

    def window_handle(self):
        # Get all window handles and switch to the second one
        all_window_handles = self.driver.window_handles
        self.driver.switch_to.window(all_window_handles[1])

    def attribute_values(self, locator):
        try:
            value = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text
            return value
        except (TimeoutException, NoSuchElementException):
            print(f"Element with locator '{locator}' not found.")
            return None

    def wait_until_element_contain_text(self, locator, text):
        try:
            return WebDriverWait(self.driver, 5).until(EC.text_to_be_present_in_element(locator, text))
        except (TimeoutException, NoSuchElementException):
            print(f"Element with locator '{locator}' not found.")
            return None

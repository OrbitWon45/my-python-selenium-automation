from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 12)

    def open_url(self, end_url=''):
        url = f'https://www.amazon.com/{end_url}'
        if end_url == '':
            self.driver.get('https://www.amazon.com/home')
        else:
            self.driver.get(url)
            sleep(2)
            self.driver.refresh()

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        e = self.find_element(*locator)
        e.send_keys(text)

    def wait_for_element_to_be_clickable_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator),
                            message= f'Element not clickable: {locator}')
        e.click()

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text == expected_text, \
            f"expected text: {expected_text}, did not match actual text: {actual_text}."

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, \
            f'expected text {expected_text} not in actual text {actual_text}'

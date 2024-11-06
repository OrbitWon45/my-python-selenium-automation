

class Page:

    def __init__(self, driver):
        self.driver = driver

    def open_url(self, end_url=''):
        url = f'https://www.amazon.com/{end_url}'
        if end_url == '':
            self.driver.get('https://www.amazon.com/exec/obidos/tg/browse/-/1055398')
            self.driver.refresh()
        else:
            self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        e = self.find_element(*locator)
        e.send_keys(text)

    def verify_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert actual_text == expected_text, \
            f"expected text: {expected_text}, did not match actual text: {actual_text}."

    def verify_partial_text(self, expected_text, *locator):
        actual_text = self.driver.find_element(*locator).text
        assert expected_text in actual_text, \
            f'expected text {expected_text} not in actual text {actual_text}'

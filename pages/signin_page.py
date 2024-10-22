from pages.base_page import Page
from selenium.webdriver.common.by import By

class SigninPage(Page):

    SIGNIN_LOGO = (By.CSS_SELECTOR, "h1.a-spacing-small")
    CONTINUE_BTN = (By.ID, 'continue')

    def verify_signin_page_is_open(self):
        self.find_element(*self.SIGNIN_LOGO)
        self.find_element(*self.CONTINUE_BTN)

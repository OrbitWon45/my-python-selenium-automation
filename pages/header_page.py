from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page


class HeaderPage(Page):

    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    CUSTOMER_SERVICE_BTN = (By.CSS_SELECTOR, 'a[href*="/gp/help/customer/display.html"]')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    POPUP_SIGNIN_BTN = (By.ID, 'nav-signin-tooltip')
    SIGNIN_BTN = (By.ID, 'nav-link-accountList-nav-line-1')
    CART_ICON = (By.ID, 'nav-cart')
    CART_COUNT = (By.ID, 'nav-cart-count')

    def search_for_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def click_signin_button(self):
        self.click(*self.SIGNIN_BTN)

    def click_signin_popup_btn(self):
        self.wait_for_element_to_be_clickable_click(*self.POPUP_SIGNIN_BTN)

    def click_on_customer_service_button(self):
        self.click(*self.CUSTOMER_SERVICE_BTN)

    def click_on_cart(self):
        self.click(*self.CART_ICON)

    def verify_cart_count(self, expected_text):
        self.verify_text(expected_text, *self.CART_COUNT)
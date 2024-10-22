from pages.base_page import Page
from selenium.webdriver.common.by import By

class ProductAndCartPage(Page):
    EMPTY_CART_MSG = (By.CSS_SELECTOR, 'h3.sc-your-amazon-cart-is-empty')

    def verify_cart_is_empty(self):
        self.find_element(*self.EMPTY_CART_MSG)

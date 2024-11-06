from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductAndCartPage(Page):
    EMPTY_CART_MSG = (By.CSS_SELECTOR, 'h3.sc-your-amazon-cart-is-empty')
    COCO_BLISS_10LB = (By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div[2]/div[1]/h2/a')
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    ADDED_TO_CART_MSG = (By.CSS_SELECTOR, 'h1.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold')
    CART_COUNT = (By.ID, 'nav-cart-count')

    def choose_a_product_coco(self):
        self.click(*self.COCO_BLISS_10LB)

    def add_to_cart_coco(self):
        self.click(*self.ADD_TO_CART_BTN)

    def verify_added_to_cart_msg(self):
        self.verify_text('Added to cart', *self.ADDED_TO_CART_MSG)

    def verify_cart_is_empty(self):
        self.verify_text('Your Amazon Cart is empty', *self.EMPTY_CART_MSG)

    def verify_cart_count(self, expected_text):
        self.verify_text(expected_text, *self.CART_COUNT)








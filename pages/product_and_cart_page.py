from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductAndCartPage(Page):
    EMPTY_CART_MSG = (By.CSS_SELECTOR, 'h3.sc-your-amazon-cart-is-empty')
    COCO_BLISS_10LB = (By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div[2]/div[1]/h2/a')
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    ADDED_TO_CART_MSG = (By.CSS_SELECTOR, 'h1.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold')
    PRODUCT_NAME = (By.ID, 'productTitle')
    CART_PRODUCT_NAME = (By.CSS_SELECTOR, 'span.a-truncate-cut')

    def choose_a_product_coco(self):
        self.click(*self.COCO_BLISS_10LB)

    def store_product_name(self):
        self.product_name = self.find_element(*self.PRODUCT_NAME).text
        print(f'Current product:{self.product_name}')

    def add_to_cart_coco(self):
        self.click(*self.ADD_TO_CART_BTN)

    def verify_added_to_cart_msg(self):
        self.verify_text('Added to cart', *self.ADDED_TO_CART_MSG)

    def verify_cart_is_empty(self):
        self.verify_text('Your Amazon Cart is empty', *self.EMPTY_CART_MSG)

    def verify_product_is_added_to_cart(self):
        expected_result = self.product_name
        actual_result = self.find_element(*self.CART_PRODUCT_NAME).text
        assert expected_result[:40] == actual_result[:40], \
            f'Expected result: {expected_result[:40]} does not match Actual result: {actual_result[:40]}'


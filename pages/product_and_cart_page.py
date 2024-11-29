from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductAndCartPage(Page):
    EMPTY_CART_MSG = (By.CSS_SELECTOR, 'h3.sc-your-amazon-cart-is-empty')
    COCO_BLISS_10LB = (By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/span/div/div/div[2]/div[1]/h2/a')
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    ADDED_TO_CART_MSG = (By.CSS_SELECTOR, 'h1.a-size-medium-plus.a-color-base.sw-atc-text.a-text-bold')
    PRODUCT_NAME = (By.ID, 'productTitle')
    CART_PRODUCT_NAME = (By.CSS_SELECTOR, 'span.a-truncate-cut')
    PRODUCT_OPTIONS = (By.CSS_SELECTOR, 'div#variation_color_name li')
    CURRENT_OPTION = (By.CSS_SELECTOR, 'span.selection')

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

    def verify_user_can_click_thr_options(self):
        expect_options = ['01-black', '02-apricot', '03-blue', '04-caramel', '05-khaki', '06-green']
        actual_options = []
        product_options = self.find_elements(*self.PRODUCT_OPTIONS)
        for option in product_options[:6]:
            option.click()
            current_option = self.find_element(*self.CURRENT_OPTION).text
            actual_options.append(current_option)
        assert expect_options == actual_options, \
            f'Expected options: {expect_options} did not match Actual options: {actual_options}'










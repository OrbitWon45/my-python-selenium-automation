from pages.base_page import Page
from selenium.webdriver.common.by import By


class ProductAndCartPage(Page):
    EMPTY_CART_MSG = (By.CSS_SELECTOR, 'h3.sc-your-amazon-cart-is-empty')
    COCO_BLISS_10LB = (By.CSS_SELECTOR, '#search > div.s-desktop-width-max.s-desktop-content.s-opposite-dir.s-wide-grid-style.sg-row > div.sg-col-20-of-24.s-matching-dir.sg-col-16-of-20.sg-col.sg-col-8-of-12.sg-col-12-of-16 > div > span.rush-component.s-latency-cf-section > div.s-main-slot.s-result-list.s-search-results.sg-row > div:nth-child(7) > div > div > div > div > span > div > div > div.s-product-image-container.aok-relative.s-text-center.s-image-overlay-grey.puis-image-overlay-grey.s-padding-left-small.s-padding-right-small.puis-spacing-small.s-height-equalized.puis.puis-v2lk1billfaou72dkme0sb0jkg6 > span > a')
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








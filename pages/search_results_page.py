from pages.base_page import Page
from selenium.webdriver.common.by import By


class SearchResultsPage(Page):
    SEARCH_RESULT = (By.XPATH, "//span[@class='a-color-state a-text-bold']")
    PRODUCT_ITEMS = (By.CSS_SELECTOR, 'span[data-csa-c-type="item"]')
    PRODUCT_ITEM_IMGS = (By.CSS_SELECTOR, 'img.s-image')
    PRODUCT_ITEM_TITLES = (By.CSS_SELECTOR, 'h2 span.a-text-normal')

    def verify_search_results(self, expected_text):
        self.verify_text(expected_text, *self.SEARCH_RESULT)

    def verify_products_have_img_and_name(self):
        all_products = self.find_elements(*self.PRODUCT_ITEMS)
        for product in all_products:
            product_title = product.find_element(*self.PRODUCT_ITEM_TITLES).text
            assert product_title, 'Product title not shown'
            product.find_element(*self.PRODUCT_ITEM_IMGS)
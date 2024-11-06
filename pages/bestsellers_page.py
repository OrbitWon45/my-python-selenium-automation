from pages.base_page import Page
from selenium.webdriver.common.by import By


class BestsellersPage(Page):

    TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')

    def verify_bestsellers_top_page_links(self, expected_amount):
        expected_amount = int(expected_amount)
        links = self.find_elements(*self.TOP_LINKS)
        assert len(links) == expected_amount, \
            f'expected {expected_amount} links but got {len(links)} links'
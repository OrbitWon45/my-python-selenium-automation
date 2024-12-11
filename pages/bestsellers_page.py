from pages.base_page import Page
from selenium.webdriver.common.by import By
from time import sleep


class BestsellersPage(Page):

    TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
    BANNER = (By.ID, 'zg_banner_text')

    def verify_bestsellers_top_page_links(self, expected_amount):
        expected_amount = int(expected_amount)
        links = self.find_elements(*self.TOP_LINKS)
        assert len(links) == expected_amount, \
            f'expected {expected_amount} links but got {len(links)} links'

    def click_thr_top_links(self):
        top_links = self.find_elements(*self.TOP_LINKS)
        for link in range(len(top_links)):
            current_link = self.find_elements(*self.TOP_LINKS)[link]
            link_text = current_link.text
            current_link.click()
            self.verify_partial_text(link_text, *self.BANNER)

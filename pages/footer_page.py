from pages.base_page import Page
from selenium.webdriver.common.by import By


class FooterPage(Page):
    FOOTER_LINKS = (By.CSS_SELECTOR, '.navFooterDescText')

    def verify_footer_links(self, expected_amount):
        expected_amount = int(expected_amount)
        links = self.find_elements(*self.FOOTER_LINKS)
        assert len(links) == expected_amount, \
            f'expect amount {expected_amount} did not match actual amount {len(links)}'
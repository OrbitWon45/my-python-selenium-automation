from pages.base_page import Page
from selenium.webdriver.common.by import By


class CustomerServicePage(Page):

    WELCOME_LOGO = (By.CSS_SELECTOR, 'h1.fs-heading.bolded')
    WELCOME_LINKS = (By.CSS_SELECTOR, 'div.issue-card-wrapper')
    TOP_LINKS = (By.CSS_SELECTOR, 'header.nav-header a')
    ALL_HELP_LINKS = (By.CSS_SELECTOR, 'li.help-topics')
    WHAT_TEXT = (By.CSS_SELECTOR, 'p.header-subtext.subtext-container')
    SEARCH_FIELD = (By.ID,'hubHelpSearchInput')
    SEARCH_TEXT = (By.CSS_SELECTOR, 'label h2.fs-heading.bolded')
    ALL_HELP_TEXT = (By.XPATH, '//h2[@class="fs-heading bolded" and text()="All help topics"]')

    def verify_customer_service_top_page_links(self, expected_amount):
        expected_amount = int(expected_amount)
        links = self.find_elements(*self.TOP_LINKS)
        assert expected_amount == len(links), \
            f'expected {expected_amount} links but got {len(links)} links'

    def verify_all_text_elements(self):
        self.verify_text('Welcome to Amazon Customer Service', *self.WELCOME_LOGO)
        self.verify_partial_text('What would you like help with today?', *self.WHAT_TEXT)
        self.verify_text('Search our help library', *self.SEARCH_TEXT)
        self.verify_text('All help topics', *self.ALL_HELP_TEXT)

    def verify_welcome_links(self, expected_amount):
        expected_amount = int(expected_amount)
        links = self.find_elements(*self.WELCOME_LINKS)
        assert expected_amount == len(links), \
            f'Expected {expected_amount} links but got {len(links)} links'

    def verify_search_field_is_displayed(self):
        self.find_element(*self.SEARCH_FIELD)

    def verify_all_help_links_are_displayed(self, expected_amount):
        expected_amount = int(expected_amount)
        links = self.find_elements(*self.ALL_HELP_LINKS)
        assert expected_amount == len(links), \
            f'Expected {expected_amount} links but got {len(links)} links'
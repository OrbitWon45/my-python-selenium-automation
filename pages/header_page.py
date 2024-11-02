from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page

class HeaderPage(Page):

    SEARCH_FIELD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    SIGNIN_BTN = (By.ID, 'nav-link-accountList-nav-line-1')
    CART_ICON = (By.ID, 'nav-cart')

    def search_for_product(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)

    def click_signin_button(self):
        self.click(*self.SIGNIN_BTN)

    def click_on_cart(self):
        self.click(*self.CART_ICON)





from pages.header_page import HeaderPage
from pages.search_results_page import SearchResultsPage
from pages.signin_page import SigninPage
from pages.product_and_cart_page import ProductAndCartPage
from pages.footer_page import FooterPage
from pages.bestsellers_page import BestsellersPage
from pages.customer_service_page import CustomerServicePage


class Application:

   def __init__(self, driver):
       self.header_page = HeaderPage(driver)
       self.search_results_page = SearchResultsPage(driver)
       self.signin_page = SigninPage(driver)
       self.product_and_cart_page = ProductAndCartPage(driver)
       self.footer_page = FooterPage(driver)
       self.bestsellers_page = BestsellersPage(driver)
       self.customer_service_page = CustomerServicePage(driver)



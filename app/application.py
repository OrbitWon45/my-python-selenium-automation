from pages.header_page import HeaderPage
from pages.search_results_page import SearchResultsPage
from pages.signin_page import SigninPage
class Application:

    def __init__(self, driver):
        self.header_page = HeaderPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.signin_page = SigninPage(driver)

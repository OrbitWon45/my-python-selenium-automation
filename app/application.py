from pages.header_page import HeaderPage
from pages.search_results_page import SearchResultsPage
class Application:

    def __init__(self, driver):
        self.header_page = HeaderPage(driver)
        self.search_results_page = SearchResultsPage(driver)

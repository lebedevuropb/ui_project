from playwright.sync_api import Page
import allure
from pages.search_box import SearchBox
from pages.catalog import Catalog
from pages.popups import Popups
from pages.header import Header



class BasePage:
    __BASE_URL = "https://action-press.ru"
    CHAT_CLOSE_BUTTON = ".closeIcon__DIjWi"

    def __init__(self, page: Page):
        self.page = page
        self._endpoint = ""
        self.search_box = SearchBox(page)
        self.catalog = Catalog(page)
        self.popups = Popups(page)
        self.header = Header(page)

    def element(self, selector):
        return self.page.locator(selector)

    def _full_url(self):
        return f"{self.__BASE_URL}{self._endpoint}"

    def navigate_to(self):
        full_url = self._full_url()
        with allure.step(f"Переход на страницу: {full_url}"):
            self.page.goto(full_url)
            self.page.wait_for_load_state('networkidle')

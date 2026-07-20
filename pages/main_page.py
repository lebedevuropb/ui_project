from playwright.sync_api import Page
from pages.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._endpoint = ""

    # селекторы
    _recommendations_title_selector = "[data-qa-locator='recommendedMagazine'] .title-text"
    _recommendation_card_selector = "[data-qa-locator='recommendedMagazine'] .card"

    # локаторы
    def recommendations_title_locator(self):
        return self.element(self._recommendations_title_selector)

    def recommendation_card_locator(self):
        return self.element(self._recommendation_card_selector)

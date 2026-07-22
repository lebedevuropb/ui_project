from playwright.sync_api import Page
from pages.personal_page import PersonalPage


class MainPage(PersonalPage):
    PAGE_URL = ""

    def __init__(self, page: Page):
        super().__init__(page)

    # селекторы
    _recommendations_title_selector = "[data-qa-locator='recommendedMagazine'] .title-text"
    _recommendation_card_selector = "[data-qa-locator='recommendedMagazine'] .card"
    _recommendation_card_price_selector = ".card-footer.d-lg-block .price-zone"
    _recommendation_card_button_selector = "[data-qa-locator='smallBasket']"

    # локаторы
    def recommendations_title_locator(self):
        return self.element(self._recommendations_title_selector)

    def recommendation_card_locator(self):
        return self.element(self._recommendation_card_selector)

    def recommendation_card_price_locator(self):
        return self.element(self._recommendation_card_price_selector)

    def recommendation_card_button_locator(self):
        return self.element(self._recommendation_card_button_selector)

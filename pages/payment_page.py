from playwright.sync_api import Page
from pages.personal_page import PersonalPage


class PaymentPage(PersonalPage):
    PAGE_URL = "/about/payment/"

    def __init__(self, page: Page):
        super().__init__(page)

    # селекторы
    _payment_cards_selector = ".payment__cards"
    _non_cash_text_selector = "//h3[normalize-space(text())='Безналичный платеж']"
    _cash_text_selector = "//h3[normalize-space(text())='Наличный платеж']"
    _card_text_selector = "//h3[normalize-space(text())='Оплата банковской картой']"
    _refound_text_selector = "//h2[normalize-space(text())='Возврат денежных средств']"
    _refound_selector = "div[class='refund']"

    # локаторы
    def payment_cards_locator(self):
        return self.element(self._payment_cards_selector)

    def non_cash_text_locator(self):
        return self.element(self._non_cash_text_selector)

    def cash_text_locator(self):
        return self.element(self._cash_text_selector)

    def card_text_locator(self):
        return self.element(self._card_text_selector)

    def refound_text_locator(self):
        return self.element(self._refound_text_selector)

    def refound_locator(self):
        return self.element(self._refound_selector)

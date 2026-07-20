from playwright.sync_api import Page
from pages.base_page import BasePage


class ContactsPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._endpoint = "/about/contacts/"

    # селекторы
    _heading_selector = ".static-page-h2"
    _feedback_title_selector = ".feedback .feedback__title"
    _feedback_messengers_selector = ".feedback__messengers a"

    # локаторы
    def heading_locator(self):
        return self.element(self._heading_selector)

    def feedback_title_locator(self):
        return self.element(self._feedback_title_selector)

    def feedback_messengers_locator(self):
        return self.element(self._feedback_messengers_selector)

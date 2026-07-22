from playwright.sync_api import Page
from pages.personal_page import PersonalPage


class ContactsPage(PersonalPage):
    PAGE_URL = "/about/contacts/"

    def __init__(self, page: Page):
        super().__init__(page)

    # селекторы
    _feedback_title_selector = ".feedback .feedback__title"
    _feedback_messengers_selector = ".feedback__messengers a"
    _map_container_selector = ".ymaps3--map-container"
    _filial_count_contact_selector = "//div[@class='filials__block_contact']"

    # локаторы
    def feedback_title_locator(self):
        return self.element(self._feedback_title_selector)

    def feedback_messengers_locator(self):
        return self.element(self._feedback_messengers_selector)

    def map_container_locator(self):
        return self.element(self._map_container_selector)

    def filials_count_locator(self):
        return self.element(self._filial_count_contact_selector)

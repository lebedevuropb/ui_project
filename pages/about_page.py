from playwright.sync_api import Page
from pages.base_page import BasePage


class AboutPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self._endpoint = "/about/"

    # селекторы
    _heading_selector = ".static-page-h2"
    _content_title_selector = ".content__title"

    # локаторы
    def heading_locator(self):
        return self.element(self._heading_selector)

    def content_title_locator(self):
        return self.element(self._content_title_selector)

    # методы
    def get_heading_text(self):
        return self.heading_locator().text_content()

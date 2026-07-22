from playwright.sync_api import Page
from pages.personal_page import PersonalPage


class AboutPage(PersonalPage):
    PAGE_URL = "/about/"

    def __init__(self, page: Page):
        super().__init__(page)

    # селекторы
    _content_title_selector = "h2[class='content__title']"
    _banner_text_title_selector = "div[class='banner__text_title']"
    _banner_description_selector = "div[class='banner__text_content']"
    _bottom_title_selector = "[class='bottom__title']"
    _bottom_devider_selector = "[class='bottom__devider']"

    # локаторы
    def content_title_locator(self):
        return self.element(self._content_title_selector)

    def banner_text_title_locator(self):
        return self.element(self._banner_text_title_selector)

    def banner_description_locator(self):
        return self.element(self._banner_description_selector)

    def bottom_title_locator(self):
        return self.element(self._bottom_title_selector)

    def bottom_devider_locator(self):
        return self.element(self._bottom_devider_selector)

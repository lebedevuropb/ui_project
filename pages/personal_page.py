from playwright.sync_api import Page
from pages.base_page import BasePage
from controls.search_box_control import SearchBoxControl
from controls.catalog_control import CatalogControl
from controls.popups_control import PopupsControl
from controls.header_control import HeaderControl


class PersonalPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.search_box = SearchBoxControl(page)
        self.catalog = CatalogControl(page)
        self.popups = PopupsControl(page)
        self.header = HeaderControl(page)

    # селекторы
    _heading_selector = ".static-page-h2"

    # локаторы
    def heading_locator(self):
        return self.element(self._heading_selector)

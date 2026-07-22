from playwright.sync_api import Page


class CatalogControl:
    def __init__(self, page: Page):
        self.page = page

    # селекторы
    _category_link_selector = "[data-qa-locator='leftMenuItem']"

    # локаторы
    def category_link_locator(self):
        return self.page.locator(self._category_link_selector)

    def category_link_by_name_locator(self, name: str):
        return self.page.locator(self._category_link_selector, has_text=name)

    # методы
    def click_category(self, name: str):
        self.category_link_by_name_locator(name).click()

    def category_names(self):
        return self.category_link_locator().all_text_contents()

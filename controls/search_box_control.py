from playwright.sync_api import Page


class SearchBoxControl:
    def __init__(self, page: Page):
        self.page = page

    # селекторы
    _click_search_selector = ".col-2-sub [data-qa-locator='desctop_top_menu_search']"
    _input_selector = ".l-ss-c-search-input-node"
    _no_results_selector = ".l-ss-c-text-caption"
    _found_count_selector = ".l-ss-c-filters-found-items"

    # локаторы
    def click_search_locator(self):
        return self.page.locator(self._click_search_selector)

    def input_locator(self):
        return self.page.locator(self._input_selector)

    def no_results_locator(self):
        return self.page.locator(self._no_results_selector)

    def found_count_locator(self):
        return self.page.locator(self._found_count_selector)

    # методы
    def type_query(self, text):
        self.click_search_locator().click()
        self.input_locator().fill(text)

    def submit(self):
        self.input_locator().press("Enter")

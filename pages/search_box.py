from playwright.sync_api import Page


class SearchBox:
    def __init__(self, page: Page):
        self.page = page

    def element(self, selector):
        return self.page.locator(selector)

    # селекторы
    _click_search_selector = (".col-2-sub .input-group.input-sub-header.l-ss-search-element-mount "
                              ".form-control.form-control-sub-header")
    _input_selector = ".l-ss-c-search-input-node"

    # локаторы
    def click_search_locator(self):
        return self.element(self._click_search_selector)

    def input_locator(self):
        return self.element(self._input_selector)

    # методы
    def type_query(self, text):
        self.click_search_locator().click()
        self.input_locator().fill(text)

    def submit(self):
        self.input_locator().press("Enter")

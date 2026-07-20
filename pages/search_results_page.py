from pages.base_page import BasePage


class SearchResultsPage(BasePage):
    # селекторы
    _no_results_selector = ".l-ss-c-text-caption"
    _found_count_selector = ".l-ss-c-filters-found-items"

    # локаторы
    def no_results_locator(self):
        return self.element(self._no_results_selector)

    def found_count_locator(self):
        return self.element(self._found_count_selector)

    # методы
    def get_no_results_text(self):
        return self.no_results_locator().text_content()

    def get_found_count_text(self):
        return self.found_count_locator().text_content()

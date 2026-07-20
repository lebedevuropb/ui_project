from playwright.sync_api import Page


class Popups:
    def __init__(self, page: Page):
        self.page = page

    def element(self, selector):
        return self.page.locator(selector)

    # селекторы
    _chat_close_selector = ".closeIcon__DIjWi"
    _subscribe_close_selector = ".p-0.outline-none"
    _cookie_accept_selector = ".btn-primary"

    # локаторы
    def chat_close_locator(self):
        return self.element(self._chat_close_selector)

    def subscribe_close_locator(self):
        return self.element(self._subscribe_close_selector)

    def cookie_accept_locator(self):
        return self.element(self._cookie_accept_selector)

    # методы
    def close_chat_widget(self):
        button = self.chat_close_locator()
        if button.is_visible():
            button.click()

    def close_subscribe_popup(self):
        button = self.subscribe_close_locator()
        if button.is_visible():
            button.click()

    def close_cookie_banner(self):
        button = self.cookie_accept_locator()
        if button.is_visible():
            button.click()

    def dismiss_all(self):
        self.close_chat_widget()
        self.close_subscribe_popup()
        self.close_cookie_banner()

from playwright.sync_api import Page
import allure


class BasePage:
    BASE_URL = "https://action-press.ru"

    def __init__(self, page: Page):
        self.page = page

    def element(self, selector):
        return self.page.locator(selector)

    def build_url(self, url=None):
        if url:
            return f"{self.BASE_URL}{url}"
        return self.BASE_URL

    def open_page(self, url=None):
        with allure.step(f"Переход на страницу: {self.build_url(url)}"):
            self.page.goto(self.build_url(url))
            self.page.wait_for_load_state('networkidle')

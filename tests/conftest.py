import pytest
from playwright.sync_api import sync_playwright
from pages.main_page import MainPage
from pages.about_page import AboutPage
from pages.contacts_page import ContactsPage
from pages.payment_page import PaymentPage


@pytest.fixture(scope="session")
def playwright_instance():
    with sync_playwright() as p:
        yield p


@pytest.fixture
def browser(playwright_instance):
    browser = playwright_instance.chromium.launch(headless=True, slow_mo=0)
    yield browser
    browser.close()


@pytest.fixture
def context(browser):
    context = browser.new_context(viewport={"width": 1440, "height": 900})
    try:
        yield context
    finally:
        context.close()


@pytest.fixture
def main_page(page):
    main_page = MainPage(page)
    main_page.open_page(MainPage.PAGE_URL)
    main_page.popups.dismiss_all()
    return main_page


@pytest.fixture
def about_page(page):
    return AboutPage(page)


@pytest.fixture
def contacts_page(page):
    return ContactsPage(page)


@pytest.fixture
def payment_page(page):
    return PaymentPage(page)

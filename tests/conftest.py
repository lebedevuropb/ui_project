import pytest
from pages.main_page import MainPage
from pages.about_page import AboutPage
from pages.contacts_page import ContactsPage
from pages.payment_page import PaymentPage


@pytest.fixture(scope="session")
def browser_type_launch_args():
    return {"headless": True, "slow_mo": 0}


@pytest.fixture
def browser_context_args():
    return {"viewport": {"width": 1440, "height": 900}}


@pytest.fixture
def main_page(page):
    main_page = MainPage(page)
    main_page.navigate_to()
    main_page.popups.dismiss_all()
    return main_page


@pytest.fixture
def about_page(page):
    about_page = AboutPage(page)
    about_page.navigate_to()
    about_page.popups.dismiss_all()
    return about_page


@pytest.fixture
def contacts_page(page):
    contacts_page = ContactsPage(page)
    contacts_page.navigate_to()
    contacts_page.popups.dismiss_all()
    return contacts_page


@pytest.fixture
def payment_page(page):
    payment_page = PaymentPage(page)
    payment_page.navigate_to()
    payment_page.popups.dismiss_all()
    return payment_page

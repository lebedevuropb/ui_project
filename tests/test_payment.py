from playwright.sync_api import expect
from utils.data import PAYMENT_HEADING, PAYMENT_URL


def test_payment_page_url(main_page):
    main_page.header.click_payment()
    expect(main_page.page).to_have_url(PAYMENT_URL)


def test_payment_page(payment_page):
    expect(payment_page.heading_locator()).to_have_text(PAYMENT_HEADING)

from playwright.sync_api import expect
from utils.data import PAYMENT_HEADING


def test_payment_page_url(main_page):
    main_page.header.click_payment()
    assert "/about/payment/" in main_page.page.url


def test_payment_page(payment_page):
    expect(payment_page.heading_locator()).to_have_text(PAYMENT_HEADING)

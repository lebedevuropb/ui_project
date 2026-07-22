from playwright.sync_api import expect
from utils.data import PAYMENT_HEADING, TITLE_PAYMENT


def test_payment_page_url(main_page, payment_page):
    main_page.header.click_payment()
    expect(main_page.page).to_have_title(TITLE_PAYMENT)
    expect(main_page.page).to_have_url(main_page.build_url(payment_page.PAGE_URL))


def test_payment_page(main_page, payment_page):
    main_page.header.click_payment()

    expect(payment_page.heading_locator()).to_have_text(PAYMENT_HEADING)
    expect(payment_page.payment_cards_locator()).to_be_visible()
    expect(payment_page.non_cash_text_locator()).to_be_visible()
    expect(payment_page.cash_text_locator()).to_be_visible()
    expect(payment_page.card_text_locator()).to_be_visible()
    expect(payment_page.refound_text_locator()).to_be_visible()
    expect(payment_page.refound_locator()).to_be_visible()

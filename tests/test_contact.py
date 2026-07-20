from playwright.sync_api import expect
from utils.data import CONTACTS_HEADING, CONTACTS_FEEDBACK_TITLE, CONTACTS_URL


def test_contacts_page_url(main_page):
    main_page.header.click_contacts()
    expect(main_page.page).to_have_url(CONTACTS_URL)


def test_contacts_page(contacts_page):
    expect(contacts_page.heading_locator()).to_have_text(CONTACTS_HEADING)
    expect(contacts_page.feedback_title_locator()).to_have_text(CONTACTS_FEEDBACK_TITLE)
    expect(contacts_page.feedback_messengers_locator()).not_to_have_count(0)

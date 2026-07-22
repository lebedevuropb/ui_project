from playwright.sync_api import expect
from utils.data import CONTACTS_HEADING, CONTACTS_FEEDBACK_TITLE, TITLE_CONTACTS


def test_contacts_page_url(main_page, contacts_page):
    main_page.header.click_contacts()
    expect(main_page.page).to_have_title(TITLE_CONTACTS)
    expect(main_page.page).to_have_url(main_page.build_url(contacts_page.PAGE_URL))


def test_contacts_page(main_page, contacts_page):
    main_page.header.click_contacts()
    expect(contacts_page.heading_locator()).to_have_text(CONTACTS_HEADING)
    expect(contacts_page.feedback_title_locator()).to_have_text(CONTACTS_FEEDBACK_TITLE)
    expect(contacts_page.feedback_messengers_locator()).not_to_have_count(0)
    expect(contacts_page.map_container_locator()).to_be_visible()
    expect(contacts_page.filials_count_locator()).not_to_have_count(0)

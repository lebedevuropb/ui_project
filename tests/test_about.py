from playwright.sync_api import expect
from utils.data import ABOUT_HEADING, ABOUT_CONTENT_TITLE


def test_about_page_url(main_page):
    main_page.header.click_about()
    assert "/about/" in main_page.page.url


def test_about_page(about_page):
    expect(about_page.heading_locator()).to_have_text(ABOUT_HEADING)
    expect(about_page.content_title_locator()).to_have_text(ABOUT_CONTENT_TITLE)

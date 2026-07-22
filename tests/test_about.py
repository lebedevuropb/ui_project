from playwright.sync_api import expect
from utils.data import ABOUT_HEADING, ABOUT_CONTENT_TITLE, TITLE_ABOUT


def test_about_page_url(main_page, about_page):
    main_page.header.click_about()
    expect(main_page.page).to_have_title(TITLE_ABOUT)
    expect(main_page.page).to_have_url(main_page.build_url(about_page.PAGE_URL))


def test_about_page(main_page, about_page):
    main_page.header.click_about()
    expect(about_page.heading_locator()).to_have_text(ABOUT_HEADING)
    expect(about_page.content_title_locator()).to_have_text(ABOUT_CONTENT_TITLE)
    expect(about_page.banner_text_title_locator()).to_be_visible()
    expect(about_page.banner_description_locator()).to_be_visible()
    expect(about_page.bottom_title_locator()).to_be_visible()
    expect(about_page.bottom_devider_locator()).to_be_visible()

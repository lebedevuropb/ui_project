from playwright.sync_api import expect


def test_header_elements_visible(main_page):
    expect(main_page.header.logo_locator()).to_be_visible()
    expect(main_page.header.phone_number_locator()).to_be_visible()
    expect(main_page.header.telegram_locator()).to_be_visible()
    expect(main_page.header.whatsapp_locator()).to_be_visible()
    expect(main_page.header.max_locator()).to_be_visible()
    expect(main_page.header.login_button_locator()).to_be_visible()
    expect(main_page.header.about_link_locator()).to_be_visible()
    expect(main_page.header.contacts_link_locator()).to_be_visible()
    expect(main_page.header.payment_link_locator()).to_be_visible()
    expect(main_page.header.deliver_link_locator()).to_be_visible()


def test_catalog_has_categories(main_page):
    expect(main_page.catalog.category_link_locator()).not_to_have_count(0)


def test_recommendations_section_has_cards(main_page):
    expect(main_page.recommendations_title_locator()).to_be_visible()
    expect(main_page.recommendation_card_locator()).not_to_have_count(0)

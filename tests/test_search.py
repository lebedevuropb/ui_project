from playwright.sync_api import expect
from utils.data import SEARCH_QUERY_NO_EXACT_MATCH, EXISTING_PRODUCT_QUERY


def test_no_results_message(main_page):
    main_page.search_box.type_query(SEARCH_QUERY_NO_EXACT_MATCH)
    expect(main_page.search_box.input_locator()).to_have_value(SEARCH_QUERY_NO_EXACT_MATCH)
    main_page.search_box.submit()
    expect(main_page.search_box.no_results_locator()).to_be_visible()


def test_successful_results(main_page):
    main_page.search_box.type_query(EXISTING_PRODUCT_QUERY)
    expect(main_page.search_box.input_locator()).to_have_value(EXISTING_PRODUCT_QUERY)
    main_page.search_box.submit()
    expect(main_page.search_box.no_results_locator()).not_to_be_visible()

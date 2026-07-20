from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage


def test_exact_query_shows_no_results_message(page):
    main_page = MainPage(page)
    main_page.navigate_to()
    main_page.popups.dismiss_all()

    main_page.search_box.type_query('Электронный журнал. ВИП-версия "Главбух" 12 мес.')
    main_page.search_box.submit()

    results_page = SearchResultsPage(page)
    message = results_page.get_no_results_text()

    assert "Товаров не найдено" in message

def test_exact_query_shows_similar_results_fallback(page):
    main_page = MainPage(page)
    main_page.navigate_to()
    main_page.popups.dismiss_all()

    main_page.search_box.type_query('Электронный журнал. ВИП-версия "Главбух" 12 мес.')
    main_page.search_box.submit()

    results_page = SearchResultsPage(page)
    message = results_page.get_found_count_text()

    assert "Найдено" in message

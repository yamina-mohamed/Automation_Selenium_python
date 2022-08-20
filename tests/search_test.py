from pages.cart import CartPage
from pages.item_details import ItemDetailsPage
from pages.result import ResultPage
from pages.search import SearchPage


def test_amazon(browser):
    search_page = SearchPage(browser)
    result_page = ResultPage(browser)
    item_details = ItemDetailsPage(browser)
    cart_page = CartPage(browser)
    phrase = "mobile"

    search_page.load()
    search_page.search(phrase)
    result_page.click_on_checkbox()
    result_page.title()
    item_details.add_to_cart()
    item_details.navigate_to_cart()
    cart_page.delete_item()









"""""




    result_page.click_on_more_btn()
    result_page.click_on_checkbox()


   for search_title in result_page.result_link_title():
        assert phrase.lower() in search_title.lower()

    assert phrase == result_page.search_input_value()

# raise Exception("Incomplete test")
"""""

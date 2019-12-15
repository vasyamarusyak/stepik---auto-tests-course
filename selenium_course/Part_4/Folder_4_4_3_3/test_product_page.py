import pytest
from .pages.product_page import ProductPage

offer_link_template = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
offer_links = [f"{offer_link_template}{i}" for i in range(5, 8)]

@pytest.mark.parametrize("link", offer_links)
def test_guest_can_add_product_to_cart_with_different_offer_numbers(browser, link: str) -> None:
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_to_cart(True)
    product_page.should_be_present_in_cart()
    product_page.should_check_overall_cost()


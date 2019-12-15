from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
import time

def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    #page.go_to_login_page()
    page.test_guest_can_add_product_to_basket()
    #time.sleep(2)
    page.solve_quiz_and_get_code()
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()
    time.sleep(100)
    #login_page = LoginPage(browser, browser.current_url)
    #login_page.should_be_login_page()

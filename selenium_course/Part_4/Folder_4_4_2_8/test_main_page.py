from .pages.main_page import MainPage
from .pages.login_page import LoginPage


link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"

def test_guest_can_go_to_login_page(browser):
    page =  MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    #page.should_be_login_form()
    #page.should_be_register_form()
    
def test_check_login_and_register(browser):
    page =  LoginPage(browser, link)
    page.open()
    page.should_be_login_page()
    #page.go_to_login_page()
    #page.should_be_login_form()
    #page.should_be_register_form()

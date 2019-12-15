#Мы можем вызывать фикстуру в тестах, передав ее как параметр.
#По умолчанию фикстура будет создаваться для каждого тестового метода,
# то есть для каждого теста запустится свой экземпляр браузера.

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    return browser


class TestMainPage1():
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print('start test link 1')
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print('start test basket 1')
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

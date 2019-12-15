#Для фикстур можно задавать область покрытия фикстур. Допустимые значения:
#“function”, “class”, “module”, “session”.
#Соответственно, фикстура будет вызываться один раз для тестового метода,
#один раз для класса, один раз для модуля или один раз для всех тестов,
#запущенных в данной сессии.

import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"

#фикстура вызвалась один раз, результат ее сохранился и использовался для всех
#методов класса, а если бы класса было бы 2 в файле, то фикстура вызвалась бы 2
#раза, по разу на каждый класc.
@pytest.fixture(scope="class")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMainPage1():

    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print("start test1")
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
        print("finish test1")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print("start test2")
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
        print("finish test2")

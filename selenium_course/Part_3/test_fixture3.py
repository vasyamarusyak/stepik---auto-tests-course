#Yield отдает свое значение (в нашем случае запущенный браузер) только когда
# есть итерируюемые объекты (в нашем случае список всех тестов).
#Как только список тестов заканчивается - yield не выполняется,
# а выполняются все действия после него.
import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


class TestMainPage1(object):
    # вызываем фикстуру в тесте, передав ее как параметр
    def test_guest_should_see_login_link(self, browser):
        print('start test link 1')
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        print('start test basket 1')
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")

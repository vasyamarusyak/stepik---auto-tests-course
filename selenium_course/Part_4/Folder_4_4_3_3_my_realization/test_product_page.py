from .pages.product_page import ProductPage
import time
import pytest

#Суть тесту полягає в тому що на кортійсь із сторінок списку нижче є баг, ми повинні його знайти.
#В тесті ми використали перевірку на повне співпадіння тексту назви книги, ціни книги на деталізації
#книги із текстом у повідомленні після додавання книги до корзини.
#Після того як баг виявлений ми - позначили осилання із багом як xfail(ожидаемо падающий).
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
                                  ])

def test_guest_can_go_to_login_page(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.test_guest_can_add_product_to_basket()
    time.sleep(1)
    page.solve_quiz_and_get_code()
    time.sleep(1)
    page.should_be_message_about_adding()
    page.should_be_message_basket_total()

#pytest  -v -s --tb=line test_product_page.py

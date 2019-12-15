from .pages.product_page import ProductPage
import time
import pytest

#Суть тесту полягає в тому що на кортійсь із сторінок списку нижче є баг, ми повинні його знайти.
#В тесті ми використали перевірку на повне співпадіння тексту назви книги, ціни книги на деталізації
#книги із текстом у повідомленні після додавання книги до корзини.
#Після того як баг виявлений ми - позначили осилання із багом як xfail(ожидаемо падающий).

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()                                #Открываем страницу товара 
    page.test_guest_can_add_product_to_basket()#Добавляем товар в корзину 
    #time.sleep(1)
    page.should_not_be_success_message()       #Проверяем, что нет сообщения об успехе с помощью is_not_element_present

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()                                 #Открываем страницу товара
    page.should_not_be_success_message()        #Проверяем, что нет сообщения об успехе с помощью is_not_element_present

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()                                #Открываем страницу товара
    page.test_guest_can_add_product_to_basket()#Добавляем товар в корзину 
    time.sleep(1)
    page.should_not_be_success_message_after_adding_product_to_basket()#Проверяем, что нет сообщения об успехе с помощью is_disappeared


#pytest  -v -s --tb=line test_product_page.py

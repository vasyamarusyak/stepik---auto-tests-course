from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time
import pytest
from .pages.login_page import LoginPage

#Суть тесту полягає в тому що деякі елементи на сторінці які є доступні по всьому флову сайту(хедер, футер і т.д) тоді
#варто створити у locators клас BasePageLocators де ми і пропишемо локатори які присутні на всьому сайті. Далі у Bsse_page
#прописуємо перевірки. і далі у test_product_page пишемо нові тести. 

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207/"

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()                                #Открываем страницу товара 
    page.test_guest_can_add_product_to_basket()#Добавляем товар в корзину 
    #time.sleep(1)
    page.should_not_be_success_message()       #Проверяем, что нет сообщения об успехе с помощью is_not_element_present

@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()                                 #Открываем страницу товара
    page.should_not_be_success_message()        #Проверяем, что нет сообщения об успехе с помощью is_not_element_present

@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()                                #Открываем страницу товара
    page.test_guest_can_add_product_to_basket()#Добавляем товар в корзину 
    time.sleep(1)
    page.should_not_be_success_message_after_adding_product_to_basket()#Проверяем, что нет сообщения об успехе с помощью is_disappeared

@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()
    #time.sleep(10)
    
@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    time.sleep(1)
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/"
    page = BasketPage(browser, link)
    page.open()                                           #Гость открывает главную страницу  
    page.test_guest_can_go_to_basket()                    #Переходит в корзину по кнопке в шапке сайта
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    print("URL method finished")
    basket_page.should_not_be_any_products_in_busket()     #Ожидаем, что в корзине нет товаров
    print("Product method finished")
    basket_page.should_be_empty_basket_page_with_text()    #Ожидаем, что есть текст о том что корзина пуста

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    page.open()                                            #Гость открывает главную страницу  
    page.test_guest_can_go_to_basket()                     #Переходит в корзину по кнопке в шапке сайта
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_url()
    print("URL method finished")
    basket_page.should_not_be_any_products_in_busket()     #Ожидаем, что в корзине нет товаров
    print("Product method finished")
    basket_page.should_be_empty_basket_page_with_text()    #Ожидаем, что есть текст о том что корзина пуста

#pytest  -v -s --tb=line test_product_page.py

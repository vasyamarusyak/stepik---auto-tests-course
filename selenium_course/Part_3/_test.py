from selenium import webdriver
import time
import unittest

class Testtest(unittest.TestCase):
    def test_test(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
       # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath("//input [contains(@class, 'form-control') and contains(@class, 'first') and @required]")
        input1.send_keys("name")

        input2 = browser.find_element_by_xpath("//input [contains(@class, 'form-control') and contains(@class, 'second') and @required]")
        input2.send_keys("surname")

        input3 = browser.find_element_by_xpath("//input [contains(@class, 'form-control') and contains(@class, 'third') and @required]")
        input3.send_keys("email")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
    
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        #assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "The text is different(((")

    def test_test_2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
       # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_xpath("//input [contains(@class, 'form-control') and contains(@class, 'first') and @required]")
        input1.send_keys("name")

        input2 = browser.find_element_by_xpath("//input [contains(@class, 'form-control') and contains(@class, 'second') and @required]")
        input2.send_keys("surname")

        input3 = browser.find_element_by_xpath("//input [contains(@class, 'form-control') and contains(@class, 'third') and @required]")
        input3.send_keys("email")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)
    
        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        #assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "The text is different(((")       
if __name__ == "__main__":
    unittest.main()

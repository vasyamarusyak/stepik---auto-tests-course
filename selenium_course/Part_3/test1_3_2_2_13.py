#тут все круто зроблено тому що коди не дублюються, і в класі
#просто підключається одна функція із різними аргументами лінків
# і коли тест падає то браузер не закривається а залишається на місці де останній
#тест проходив до падіння
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

browser = webdriver.Chrome()

def registration(link):
    browser.get(link)
    input1 = browser.find_element_by_css_selector(".first_block .first")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector(".first_block .second")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector(".first_block .third")
    input3.send_keys("test@mail.ru")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    return welcome_text_elt.text

class TestRegistr(unittest.TestCase):
    def test_registr1(self):
        link = "http://suninjuly.github.io/registration1.html"
        self.assertEqual(registration(link), "Congratulations! You have successfully registered!")

    def test_registr2(self):
        link = "http://suninjuly.github.io/registration2.html"
        self.assertEqual(registration(link), "Congratulations! You have successfully registered!")
        
if __name__ == "__main__":
    unittest.main()

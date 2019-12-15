from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

browser = webdriver.Chrome()

def registration(link):
    browser.get(link)
    textBox1 = browser.find_element(By.XPATH, "//input[@placeholder='Email']")
    input1.send_keys("admin@gmail@com")
    textBox2 = browser.find_element(By.XPATH, "//input[@placeholder='Пароль']")
    input2.send_keys("admin")

    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    #welcome_text_elt = browser.find_element_by_tag_name("h1")
    #return welcome_text_elt.text

class TestRegistr(unittest.TestCase):
    def test_registr1(self):
        link = "https://static.fishkaapp.net/login"
        self.assertEqual(registration(link), "Congratulations! You have successfully registered!")

  if __name__ == "__main__":
    unittest.main()

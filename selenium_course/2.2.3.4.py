from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

browser = webdriver.Chrome()
browser.get(link)

#click on the button
button = browser.find_element_by_css_selector("button.btn")
button.click()

#the confirm alert appear. Switch to alert and click on the confirm button on it.
confirm = browser.switch_to.alert
confirm.accept()

#calculate function
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

#витягуємо значення х із сторінки
x_element = browser.find_element_by_id("input_value")
x = x_element.text

y = calc(x)
answer = browser.find_element_by_id("answer")
answer.send_keys(y)

#click on the button
button = browser.find_element_by_css_selector("button.btn")
button.click()

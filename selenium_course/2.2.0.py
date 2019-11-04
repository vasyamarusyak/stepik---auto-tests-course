from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/math.html"


browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

x_element = browser.find_element_by_id("input_value")
x = x_element.text
y = calc(x)
    

answer = browser.find_element_by_id("answer")
answer.send_keys(y)

option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()

option2 = browser.find_element_by_css_selector("[value='robots']")
option2.click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

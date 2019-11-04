from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

browser = webdriver.Chrome()
browser.get(link)

#обраховуємо функцію
def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

#витягуємо значення х із сторінки
x_element = browser.find_element_by_id("input_value")
x = x_element.text

#записуємо змінну y у поле відповіді
y = calc(x)
answer = browser.find_element_by_id("answer")
answer.send_keys(y)

#знаходимо елемент за тегом і скрлимо до нього
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)

#click on a check_box
option1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
option1.click()

#click on a certain radio button
option2 = browser.find_element_by_css_selector("[value='robots']")
option2.click()

#find button again and click on it
button = browser.find_element_by_css_selector("button.btn")
button.click()

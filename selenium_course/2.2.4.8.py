from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд, поки текст в елементі price не стане рівним $100 
price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        )
button_1 = browser.find_element_by_id("book")
button_1.click()

#знаходимо елемент за тегом і скрлимо до нього
button_2 = browser.find_element_by_id("solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button_2)

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

button_2.click()


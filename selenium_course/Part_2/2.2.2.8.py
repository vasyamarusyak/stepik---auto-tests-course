import os 
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math

link = "http://suninjuly.github.io/file_input.html"

browser = webdriver.Chrome()
browser.get(link)

#fill first field
first = browser.find_element_by_name("firstname")
first.send_keys("Vasya")

#fill last field
last = browser.find_element_by_name("lastname")
last.send_keys("Lastname")

#fill email field
email = browser.find_element_by_name("email")
email.send_keys("email@i.ua")


#download your file to the register form(file must locate at the same folder as your exsecute file)
current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
file_path = os.path.join(current_dir, 'Entry.txt')           # добавляем к этому пути имя файла 
element = browser.find_element_by_name("file")
element.send_keys(file_path)


#click on a submit button
button = browser.find_element_by_css_selector("button.btn")
button.click()

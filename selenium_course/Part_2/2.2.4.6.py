from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/cats.html")

time.sleep(1)
button = browser.find_element_by_id("button")
button.click()

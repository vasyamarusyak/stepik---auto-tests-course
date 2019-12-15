from selenium import webdriver
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

browser = webdriver.Chrome()
browser.get(link)


x_element = browser.find_element_by_id("num1")
x = x_element.text


y_element = browser.find_element_by_id("num2")
y = y_element.text


sum1 = str(int(x)+int(y))
           
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_visible_text(sum1)
#select.click()
#list1 = browser.find_element_by_tag_name("select").click()
#list_select = browser.select.select_by_visible_text(sum1).click()
#browser.find_element_by_css_selector("[value='sum1']").click()

button = browser.find_element_by_css_selector("button.btn")
button.click()

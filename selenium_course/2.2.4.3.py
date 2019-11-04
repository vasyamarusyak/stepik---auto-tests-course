from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")
#set time deley because the button appears with some dele and selenium can't find it
time.sleep(2)


button = browser.find_element_by_id("verify")
button.click()


time.sleep(2)
message = browser.find_element_by_id("verify_message")

#make check with text inside the field
assert "Verification was successful!" in message.text

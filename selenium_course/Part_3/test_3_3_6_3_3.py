import math
import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('URL_ADDRESS', 
["https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1"])
def test_guest_should_see_login_link(browser, URL_ADDRESS):
    link = "{}".format(URL_ADDRESS)
    browser.get(link)
    time.sleep(6)
    browser.find_element_by_class_name("textarea").send_keys(str(math.log(int(time.time()))))
    browser.find_element_by_class_name("submit-submission").click()
    time.sleep(6)
    message = browser.find_element_by_class_name("smart-hints__hint")
    assert "Correct!" == message.text, f'Expected "Correct!", actual result "{message.text}"'

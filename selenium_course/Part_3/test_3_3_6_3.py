from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import math
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    browser.implicitly_wait(10)
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ["236895","236896","236897","236898","236899","236903","236904","236905"])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    
    answer = str(math.log(int(time.time())))
    browser.find_element_by_tag_name('textarea').send_keys(answer)
    #browser.find_element_by_css_selector(".textarea").send_keys(answer)
    button = browser.find_element_by_class_name("submit-submission")
    button.click()
 
    #expected_result = "Correct!"
    hint = browser.find_element_by_class_name("smart-hints__hint")
    
    x = hint.text
    print(x)
    feedback = browser.find_element_by_css_selector('pre.smart-hints__hint').text
    assert feedback == 'Correct!', 'This is part of alient message: ' + feedback


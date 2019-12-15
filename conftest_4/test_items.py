import time
from selenium.webdriver.common.by import By

#def test_user_can_add_item_to_basket(browser):
    #link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    #browser.get(link)
   # time.sleep(30)
   # link = browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')

    #link.click()


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_button_add_to_basket_exists(browser):
    browser.get(link)
    time.sleep(30)
    btn_add_to_basket = browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
    #assert btn_add_to_basket != None
    try:
        browser.find_element_by_css_selector(".btn-add-to-basket")
    except NoSuchElementException:
        pytest.fail("There is no such element")

#def test_guest_should_see_login_link_fail(browser):
    #browser.get(link)
    #browser.find_element_by_css_selector("#magic_link")

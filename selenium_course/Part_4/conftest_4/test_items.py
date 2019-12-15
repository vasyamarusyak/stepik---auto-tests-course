import time

def test_user_can_add_item_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    link = browser.find_element_by_css_selector('.btn.btn-lg.btn-primary.btn-add-to-basket')
    link.click()

#def test_guest_should_see_login_link_fail(browser):
    #browser.get(link)
    #browser.find_element_by_css_selector("#magic_link")

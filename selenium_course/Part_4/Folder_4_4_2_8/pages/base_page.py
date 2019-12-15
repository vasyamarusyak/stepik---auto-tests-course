from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException


from .locators import MainPageLocators
from .locators import BasePageLocators


class BasePage():
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)
        
    def open(self):
        self.browser.get(self.url)
        
    #def is_element_present(self, By.CSS_SELECTOR, "#login_link"):
     #   try:
      #      self.browser.find_element(By.CSS_SELECTOR, "#login_link")
       # except (NoSuchElementException):
        #    return False
        #return True

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoAlertPresentException
from .locators import MainPageLocators
from .locators import BasePageLocators
import math
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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

    def solve_quiz_and_get_code(self):
        #WebDriverWait(self.browser, 3).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        print(answer)
        alert.send_keys(answer)
        alert.accept()
        try:
          #  WebDriverWait(self.browser, 3).until(EC.alert_is_present())
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

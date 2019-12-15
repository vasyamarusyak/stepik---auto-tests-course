from selenium.webdriver.common.by import By

class BasePageLocators(object):
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    
class LoginPageLocators():
    L_FORM = (By.CSS_SELECTOR, "#login_form") 
    R_FORM = (By.CSS_SELECTOR, "#register_form")


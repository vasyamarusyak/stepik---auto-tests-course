from Folder_4_4_2_5 .pages.base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def go_to_login_page(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "The element is not finded"
        LOGIN_LINK.click()
        
    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

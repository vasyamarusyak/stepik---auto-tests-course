from Folder_4_4_2_5 .pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage):
    def should_be_login_link(self):
        self.browser.find_element(By.CSS_SELECTOR, "#login_link_invalid")

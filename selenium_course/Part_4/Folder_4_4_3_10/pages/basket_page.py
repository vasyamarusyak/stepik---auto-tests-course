from .base_page import BasePage
from .locators import BasePageLocators
from .locators import BasketPageLocators
import pytest

class BasketPage(BasePage):    
# Перевіряємо правильність url 
    def should_be_basket_url(self):
        assert "/basket/" in self.browser.current_url, "MAY BE NOT 'basket' PAGE"

# Сначала проверяем, что элементы присутствуют на странице, а потім витягуємо повідомлення що корзина пуста,
# і порівнюємо із еталонним значенням.
    def should_be_empty_basket_page_with_text(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), (
            "Message about empty basket is not presented")
        text_in_message = self.browser.find_element(*BasketPageLocators.MESSAGE_EMPTY_BASKET).text
        message = "Your basket is empty. Continue shopping"
        assert text_in_message == message, \
             f"The alert contains text in message: {message} - {text_in_message}"

    def should_not_be_any_products_in_busket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_WITH_PRODUCTS), \
        "Success message is presented, but should not be"






        


from pages.base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import time 

class ProductPage(BasePage):
    def add_product_to_basket(self):
        try:
            self.browser.implicitly_wait(5)
            basket_button = self.browser.find_element(*ProductPageLocators.BASKET_BUTTON)
            basket_button.click()
        except NoSuchElementException:
            print("Basket element not found")

        try:
            self.solve_quiz_and_get_code()
        except NoAlertPresentException:
            print("No alert appeared")

    def naming_equality(self):
        assert self.title_alert == self.title_description, 'Naming is the same'

    def check_price_equality(self):
        assert self.book_price == self.total_price, 'Price is the same'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is presented, but should not be"

    def should_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), "Success message is not disappeared, but should disappeared"


 

from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    product_url = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form [type='submit']")
    TITLE_ALERT = (By.CSS_SELECTOR, ".row h1")
    TITLE_DESCRIPTION = (By.CSS_SELECTOR, ".alertinner>strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    TOTAL_PRICE = (By.CLASS_NAME, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")

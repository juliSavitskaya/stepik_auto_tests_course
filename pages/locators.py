from selenium.webdriver.common.by import By

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASS_REGISTER = (By.CSS_SELECTOR, "#id_registration-password1")
    PASS_CONFIRM = (By.CSS_SELECTOR, "#id_registration-password2")
    BUTTON_REGISTR = (By.CSS_SELECTOR, "#register_form button")

class ProductPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, "#add_to_basket_form [type='submit']")
    TITLE_ALERT = (By.CSS_SELECTOR, ".row h1")
    TITLE_DESCRIPTION = (By.CSS_SELECTOR, ".alertinner>strong")
    BOOK_PRICE = (By.CSS_SELECTOR, "p.price_color")
    TOTAL_PRICE = (By.CLASS_NAME, ".alertinner p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success")
    
class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a:nth-child(1)")

class BasketPageLocators():
    TEXT_EMPTY_BASKET = (By.CSS_SELECTOR, "#content_inner > p")
    MSG_EMPTY_BASKET = (By.CSS_SELECTOR, ".basket-items .row .col-sm-4 h3")

from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_url = self.browser.current_url
        assert "login" in self.browser.current_url, "Login url is not presented"
        assert True

    def go_to_login_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.LOGIN_FORM)
        login_form.click()    

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented" 
        assert True

    def go_to_register_form(self):
        login_form = self.browser.find_element(*LoginPageLocators.REGISTER_FORM)
        register_link.click()  

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented" 
        assert True

    def register_new_user(self, email, password):
        self.go_to_login_page()
        email_field = self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)
        pass1_field = self.browser.find_element(*LoginPageLocators.PASS_REGISTER)
        pass1_field.send_keys(password)
        pass2_field = self.browser.find_element(*LoginPageLocators.PASS_CONFIRM)
        pass2_field.send_keys(password)
        button_registr = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTR)
        button_registr.click()	 

from pages.product_page import ProductPage
import time
from pages.locators import ProductPageLocators
from pages.base_page import BasePage
import pytest

initial_url = ProductPageLocators.product_url
urls = [f"{initial_url}/?promo=offer{no}" for no in range(10)]

@pytest.mark.parametrize('link', urls)
def test_guest_can_add_product_to_basket(browser, link):
    link = ProductPageLocators.product_url
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()

    
@pytest.mark.xfail(reason="fixing this bug")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.add_product_to_basket()
    product_page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.open()
    product_page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    product_page.add_product_to_basket()
    product_page.should_disappeared_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()



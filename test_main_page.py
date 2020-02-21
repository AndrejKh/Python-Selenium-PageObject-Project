from Pages.main_page import MainPage
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.base_page import BasePage
from Pages.main_page import MainPage
import pytest


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = MainPage(browser, link)
    page.open()
    login_page = LoginPage(browser, link)
    login_page.should_be_login_page(browser)


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = BasePage(browser, link)
    page.open()
    page.guest_cant_see_product_in_basket()
    page.guest_can_see_the_status_message()




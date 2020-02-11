from Pages.base_page import BasePage
from Pages.login_page import LoginPage
import pytest
from Pages.product_page import PageObject
from selenium import webdriver
import time
from Pages.locators import PageObjectLocators

links = [
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                              pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                              marks=pytest.mark.xfail),
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9", ]


@pytest.mark.parametrize('link', links)

def test_guest_can_add_product_to_basket(browser, link):
     page = PageObject(browser, link)
     page.open()
     page.should_be_add_to_cart_button()
     page.solve_quiz_and_get_code()
     page.should_be_success_message()


def should_be_success_message(self):
    x = self.browser.find_element_by_css_selector(PageObjectLocators.ITEM_NAME[1]).text
    y = self.browser.find_element_by_css_selector(PageObjectLocators.NAME[1]).text
    assert (str(y)) == (str(x))

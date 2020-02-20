from selenium.webdriver.common.by import By
from Pages.locators import PageObjectLocators
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from .locators import BasePageLocators


class BasePage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(10)

    def go_to_login_page(self, browser, link):
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK_INVALID)
        link.click()

    def should_be_login_link(self, browser, link):
        self.link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"

    def is_element_present(self, *args):
        try:
            self.browser.find_element_by_css_selector(args[1])
        except Exception as e:
            return False
        else:
            return True

    def open(self):
        self.browser.get(self.link)

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def guest_cant_see_product_in_basket(self):
        self.link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
        button = self.browser.find_element_by_css_selector(BasePageLocators.CLICK_ON_BASKET[1])
        button.click()
        assert button

    def guest_can_see_the_status_message(self):
        text = self.browser.find_element_by_xpath(BasePageLocators.EMPTY_BASKET[1]).text
        assert text


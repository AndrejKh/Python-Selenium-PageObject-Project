from selenium.webdriver.common.by import By
from selenium import webdriver
from .login_page import LoginPage
from Pages.base_page import BasePage
from Pages.locators import MainPageLocators
import pytest


class MainPage(BasePage):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_form(self):
        login_form = self.browser.find_element_by_css_selector("form#login_form.well"), "Can't find any login form"
        assert login_form

    def should_be_register_form(self):
        register_form = self.browser.find_element_by_css_selector("form#register_form.well"), "Can't find any registration form"
        assert register_form

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(self, browser, link)
        self.browser.get(self.link)
        page.open()
        page.should_be_login_link()



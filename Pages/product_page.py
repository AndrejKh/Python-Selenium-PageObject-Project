import pytest
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Pages.login_page import LoginPage
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from Pages.locators import PageObjectLocators
import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from Pages.locators import ProductPageLocators


class ProductPage(BasePage):

    def should_be_add_to_cart_button(self):
        self.browser.find_element_by_css_selector(PageObjectLocators.CLICK_THE_BUTTON[1]).click()
        assert True

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_success_message(self):
        x = self.browser.find_element_by_css_selector(PageObjectLocators.ITEM_NAME[1]).text
        y = self.browser.find_element_by_css_selector(PageObjectLocators.NAME[1]).text
        assert (str(y)) == (str(x))

    def test_guest_cant_see_success_message_after_adding_product_to_basket(self):
        assert self.is_not_element_present(*ProductPageLocators.GET_AN_ALERT), \
            "Success message is presented, but should not be"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.GET_AN_ALERT), \
            "Success message is presented, but should not be"

    def should_disappear_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.GET_AN_ALERT), \
           "Success message should disappear"
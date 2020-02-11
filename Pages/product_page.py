import pytest
from selenium.webdriver.common.by import By
from Pages.base_page import BasePage
from Pages.login_page import LoginPage
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from Pages.locators import PageObjectLocators
import math
import time

class PageObject(BasePage):

    def __init__(self, browser, links):
        super().__init__(browser, links)


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

    def should_be_success_message(self):
        x = self.browser.find_element_by_css_selector(PageObjectLocators.ITEM_NAME[1]).text
        y = self.browser.find_element_by_css_selector(PageObjectLocators.NAME[1]).text
        assert (str(y)) == (str(x))



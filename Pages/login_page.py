from Pages.base_page import BasePage
from selenium import webdriver
import math
from selenium.common.exceptions import NoAlertPresentException
import pytest


class LoginPage(BasePage):
    def __init__(self):
        self.browser = webdriver.Chrome()

    def test_guest_can_go_to_page(self, browser, link):
        browser.get(link)
        browser.imlicitly_wait(5)

    def should_be_add_to_cart_button(self):
        button = self.browser.find_element_by_css_selector("button.btn.btn-lg.btn-primary.btn-add-to-basket")
        assert button
        button.click

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


def add_product_to_cart(browser):
    item = browser.find_element_by_css_selector()
    assert item


def should_be_success_message(expected_result, actual_result):
    assert expected_result == actual_result, f'expected {expected_result}, got {actual_result}'

from Pages.base_page import BasePage
from selenium import webdriver
import math
from selenium.common.exceptions import NoAlertPresentException
import pytest
browser = webdriver.Chrome
from Pages.locators import BasePageLocators
from Pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self, browser):
        login_page = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        browser.get(login_page)
        assert login_page

    def should_be_login_form(self):
        login_form = self.browser.find_element_by_css_selector("form#login_form.well"), "Can't find any login form"
        assert login_form

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

    def register_new_user(self, browser,link):
        self.browser.get(link)
        browser.find_element_by_css_selector(LoginPageLocators.CLICK_LOGIN[1]).click()
        browser.find_element_by_css_selector(LoginPageLocators.INPUT_EMAIL[1]).send_keys("vas@gmail.com")
        browser.find_element_by_css_selector(LoginPageLocators.INPUT_PASSWORD[1]).send_keys("12345local")
        browser.find_element_by_css_selector(LoginPageLocators.CONFIRM_PASSWORD[1]).send_keys("12345local")
        browser.find_element_by_css_selector(LoginPageLocators.REGISTER_BUTTON[1]).click()


@pytest.fixture(scope="function", autouse=True)
def setup(self):
    link = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    self.page = self.browser.get(link)
    browser.find_element_by_css_selector(*LoginPageLocators.INPUT_EMAIL).send_keys("vas@gmail.com")
    browser.find_element_by_css_selector(*LoginPageLocators.INPUT_PASSWORD).send_keys("12345local")
    browser.find_element_by_css_selector(*LoginPageLocators.CONFIRM_PASSWORD).send_keys("12345local")
    browser.find_element_by_css_selector(*LoginPageLocators.REGISTER_BUTTON).click()
    assert self.is_element_present(*BasePageLocators.USER_ICON), "User icon is not presented," \
                                                                 " probably unauthorised user"


def add_product_to_cart(browser):
    item = browser.find_element_by_css_selector()
    assert item


def should_be_success_message(expected_result, actual_result):
    assert expected_result == actual_result, f'expected {expected_result}, got {actual_result}'


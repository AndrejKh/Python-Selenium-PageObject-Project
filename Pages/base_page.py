from selenium.webdriver.common.by import By
from Pages.locators import PageObjectLocators
import pytest

class BasePage:
    def __init__(self, browser, link):
        self.browser = browser
        self.link = link
        self.browser.implicitly_wait(10)

    def is_element_present(self):
        self.browser.find_element_by_css_selector(PageObjectLocators.CLICK_THE_BUTTON[1])
        assert True

    def open(self):
        self.browser.get(self.link)



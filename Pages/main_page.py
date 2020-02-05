from selenium.webdriver.common.by import By

from Pages.base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element_by_css_selector("#login_link")
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"

    def is_element_present(self, how, what):
        assert self.is_element_present(By.CSS_SELECTOR - how, "#login_link" - what)

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(self, browser, link)
        self.browser.get(self.link)
        page.open()
        page.should_be_login_link()



from Pages.base_page import BasePage

from Pages.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login_link = self.browser.find_element_by_css_selector("a#login_link"), "Login link is not presented"
        login_link.click()

        print(self.browser.current_url)

        assert self.is_element_present(*LoginPageLocators.LOGIN_LINK), "Login link is not presented"

    def should_be_login_form(self):
        login_form = self.broswer.find_element_by_css_selector("form#login_form.well"), "Can't find any login form"
        assert login_form

    def should_be_register_form(self):
        register_form = self.broswer.find_element_by_css_selector("form#register_form.well"), "Can't find any registration form"
        assert register_form

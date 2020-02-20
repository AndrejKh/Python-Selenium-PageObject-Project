from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "form#login_form.well")
    REGITSER = (By.CSS_SELECTOR, "form#register_form.well")

class PageObjectLocators():
    CLICK_THE_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket") 
    ITEM_NAME=(By.CSS_SELECTOR,'div.alertinner strong')
    NAME=(By.CSS_SELECTOR,"div h1")  

class ProductPageLocators():
    GET_AN_ALERT = (By.CSS_SELECTOR, "div.alertinner") 
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket") 

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    CLICK_ON_BASKET = (By.CSS_SELECTOR, "div.basket-mini.pull-right.hidden-xs > span > a")
    EMPTY_BASKET = (By.XPATH, "//p[contains(text(), 'empty')]")



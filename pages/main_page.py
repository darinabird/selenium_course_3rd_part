from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def go_to_login_page(self):

        link = self.browser.find_element(*MainPageLocators.login_link)
        link.click()
        # return LoginPage(browser=self.browser, url=self.browser.current_url)

    # метод проверяющий наличие ссылки

    def should_be_login_link(self):
        assert self.is_element_present(
            *MainPageLocators.login_link), "Login link isn't presented"

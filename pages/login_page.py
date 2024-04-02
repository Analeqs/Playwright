from playwright.sync_api import Page, expect
from pages.base_page import BasePage


class LoginPage(BasePage):
    EMAIL_SELECTOR = '//*[@type="email"]'
    PASSWORD = '//*[@type="password"]'
    SIGN_IN = '//*[@type="submit"]'

    def __init__(self, page: Page):
        super().__init__(page)

    def fill_email(self, email: object) -> object:
        self.fill_element(self.EMAIL_SELECTOR, value=email)

    def fill_password(self, password):
        self.fill_element(self.PASSWORD, value=password)

    def sigh_in(self):
        self.click_element(self.SIGN_IN)

from playwright.sync_api import Page, expect

import pages.login_page
from pages.base_page import BasePage
from pages.login_page import LoginPage


class AccountPage(BasePage):
    ACCOUNTS = '//a[normalize-space()="Accounts"]'
    ADD_ACCOUNT = '//button[normalize-space()="Add Account"]'
    ACCOUNT_NUMBER = '//input[@placeholder="accountNumber"]'
    CURRENCY = '//input[@id="currency"]'

    DESCRIPTION = '//input[@id="description"]'
    BALANCE = '//input[@id="balance"]'
    ADD = '//button[@class="max-modal_mobile_max:w-full disabled:bg-body text-white bg-primary hover:bg-gradient-to-br focus:ring-4 focus:outline-none focus:ring-blue-300 dark:focus:ring-blue-800 font-medium rounded-lg text-sm px-5 py-2.5 text-center mr-2"]'

    def __init__(self, page: Page):
        super().__init__(page)

    def add_account(self, account_number, currency, description, balance):
        self.click_element(self.ACCOUNTS)
        self.click_element(self.ADD_ACCOUNT)
        self.click_element(self.ACCOUNT_NUMBER )
        self.fill_element(self.ACCOUNT_NUMBER, value=account_number)
        self.fill_element(self.CURRENCY, value=currency)
        self.fill_element(self.DESCRIPTION, value=description)
        self.fill_element(self.BALANCE, value=balance)
        self.click_element(self.ADD)

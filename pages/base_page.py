from playwright.sync_api import Page, expect


class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def get_element(self, selector):
        return self.page.locator(selector)

    def click_element(self, selector):
        self.get_element(selector).click()

    def fill_element(self, selector, value):
        self.get_element(selector).fill(value=value)

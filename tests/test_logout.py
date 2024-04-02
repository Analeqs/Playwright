import re

from playwright.sync_api import Page, expect
from pages.base_page import BasePage
from pages.account_page import AccountPage
from pages.login_page import LoginPage
from pages.menu_page import MenuPage


def test_log_out(page: Page):
    page.goto(url="http://165.227.132.1/login")
    account_page = AccountPage(page)
    login_page = LoginPage(page)
    menu_page = MenuPage(page)
    dropdown_menu = account_page.get_element('//a[@class="flex items-center gap-4"]//*[name()="svg"]')
    log_out = page.locator(
        '//button[@class="flex items-center gap-3.5 py-4 px-6 text-sm font-medium duration-300 ease-in-out '
        'hover:text-primary lg:text-base"]')
    main_page = page.locator('//span[@class="mb-1.5 block font-medium"]')
    login_page.fill_email("anahitaleqs89@gmail.com")
    login_page.fill_password("Ashun2024!")
    login_page.sigh_in()
    menu_page.click_accounts_menu()
    account_page.add_account(account_number="1234555555551234", currency="USD", description="Deposit", balance="300")
    # page.pause()

    dropdown_menu.click()
    log_out.click()

    expect(main_page).to_have_text("Start for free")
    page.goto('http://165.227.132.1/accounts')
    expect(page).not_to_have_url('/accounts')
    expect(page).to_have_url(re.compile(".*/login"))

from playwright.sync_api import Page, expect
import time

from pages.account_page import AccountPage
from pages.login_page import LoginPage

def test_correct_name(page:Page):
    page.goto(url="http://165.227.132.1/login")
    login_page=LoginPage(page)
    account_page=AccountPage(page)
    login_page.fill_email("anahitaleqs89@gmail.com")
    login_page.fill_password("Ashun2024!")
    login_page.sigh_in()
    account_page.add_account("1111 1111 1111 1111","USD", "saving", "5000")






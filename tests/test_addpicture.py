from playwright.sync_api import Page, expect
import time
from pages.login_page import LoginPage


def test_login(page :Page):
    page.goto(url="http://165.227.132.1/login")
    login_page = LoginPage(page)
    login_page.fill_email("anahitaleqs89@gmail.com")
    login_page.fill_password("Ashun2024!")
    login_page.sigh_in()

    avatar = page.locator('//a[@class="flex items-center gap-4"]//*[name()="svg"]')
    profile = page.locator('//a[normalize-space()="My Profile"]')
    add_pic = page.locator('//label[@for="profile"]//*[name()="svg"]')
    avatar.click()
    profile.click()
    add_pic.click()
    input_selector = 'input[type="file"]'
    file_path = 'test.jpg'
    page.input_file(input_selector, file_path)

    time.sleep(10)

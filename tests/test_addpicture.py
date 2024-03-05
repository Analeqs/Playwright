from playwright.sync_api import Page, expect
import time


def test_login(page:Page):
    page.goto(url="http://165.227.132.1/login")
    email = page.locator('//*[@type="email"]')
    password=page.locator('//*[@type="password"]')
    sign_in = page.locator('//*[@type="submit"]')
    avatar= page.locator('//a[@class="flex items-center gap-4"]//*[name()="svg"]')
    profile=page.locator('//a[normalize-space()="My Profile"]')
    add_pic=page.locator('//label[@for="profile"]//*[name()="svg"]')
    email.fill("anahitaleqs89@gmail.com")
    password.fill("Ashun2024!")
    sign_in.click()
    avatar.click()
    profile.click()
    add_pic.click()
    input_selector = 'input[type="file"]'
    file_path = 'C:\\Users\\anahi\\Downloads\\test.jpg'
    page.input_file(input_selector, file_path)

    time.sleep(10)

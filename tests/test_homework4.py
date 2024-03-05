from playwright.sync_api import Page, expect
import time

# def test_wrong_user(page:Page):
#     page.goto(url="http://165.227.132.1/login")
#     email=page.locator('//*[@type="email"]')
#     password=page.locator('//*[@type="password"]')
#     sign_in=page.locator('//*[@type="submit"]')
#     error_text=page.locator('//span[@class="mb-1.5 block font-medium text-red-900"]')
#     email.fill("an@gmail.com")
#     password.fill("Ashun2024!")
#     sign_in.click()
#     print(error_text.text_content())

# def test_wrong_password(page:Page):
#     page.goto(url="http://165.227.132.1/login")
#     email=page.locator('//*[@type="email"]')
#     password=page.locator('//*[@type="password"]')
#     sign_in=page.locator('//*[@type="submit"]')
#     error_text=page.locator('//span[@class="mb-1.5 block font-medium text-red-900"]')
#     email.fill("anahitaleqs89@gmail.com")
#     password.fill("Ashun204!")
#     sign_in.click()
#     print(error_text.text_content())


# def test_wrong_user_pass(page:Page):
#     page.goto(url="http://165.227.132.1/login")
#     email = page.locator('//*[@type="email"]')
#     password = page.locator('//*[@type="password"]')
#     sign_in = page.locator('//*[@type="submit"]')
#     error_text = page.locator('//span[contains(text(),"Password must be at least 8 characters long and co")]')
#     email.fill("ahiale89@gmail.com")
#     password.fill("Ashu24!")
#     sign_in.click()
#     assert error_text
#     print(error_text.text_content())





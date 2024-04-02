import time

from playwright.sync_api import Page,expect
from time import perf_counter

def test_subscribe(page:Page):
    page.goto(url="http://165.227.132.1/login")
    sign_up= page.locator('a[Class="text-primary"]')
    first_name=page.locator('//*[@name="firstName"]')
    last_name=page.locator('//*[@name="lastName"]')
    user_name=page.locator('//*[@name="username"]')
    email=page.locator('//*[@name="email"]')
    password=page.locator('//*[@name="password"]')
    re_enter_password=page.locator('//*[@name="retype"]')
    create_account=page.locator('//*[@type="submit"]')
    sign_up.click()
    first_name.fill("Anahit")
    last_name.fill("Aleksanyan")
    user_name.fill("Analeqs")
    email.fill("anahitaleqs89@gmail.com")
    password.fill("Ashun2024!")
    re_enter_password.fill("Ashun2024!")
    create_account.click()
    time.sleep(10)
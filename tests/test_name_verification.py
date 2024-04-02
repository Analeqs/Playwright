import time

from playwright.sync_api import Page, expect
from pages.login_page import LoginPage


def test_correct_name(page:Page):
    page.goto(url="http://165.227.132.1/login")
    login_page=LoginPage(page)

    menu = page.locator('a[class="active"] img[alt="Logo"]')
    profile=page.locator('body > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > aside:nth-child(1) > div:nth-child(2) > nav:nth-child(1) > div:nth-child(1) > ul:nth-child(2) > li:nth-child(2) > a:nth-child(1)')
    profile_owner= page.locator('//h3[@class="mb-1.5 text-2xl font-semibold text-black dark:text-white flex justify-center items-center"]')
    login_page.fill_email(email="anahitaleqs89@gmail.com")
    login_page.fill_password("Ashun2024!")
    login_page.sigh_in()
    menu.click()
    profile.click()
    real_profile_owner="Anahit Aleksanyan"
    assert profile_owner.text_content()== real_profile_owner
    # expect(profile_owner).to_have_text(real_profile_owner, timeout=10000)

    print(f'Yes the profile owner is {real_profile_owner }.')






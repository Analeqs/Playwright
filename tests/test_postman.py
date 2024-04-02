from playwright.sync_api import Page, expect


def test_login(page: Page):
    page.goto(url="https://www.postman.com/")
    expect(page).to_have_title("Postman API Platform | Sign Up for Free")
    # xpath = '//*[text()="Explore the Public API Network →"]'
    # link = page.get_by_role('link', name="Explore the Public API Network →", exact=True)

    sign_up_xpath = '//*[text()="Sign Up for Free"]'
    email_scc_path = 'input[id="email"]'
    username_scc_path = 'input[id="username"]'
    password_scc_path = 'input[id="password"]'
    free_account_scc_path = '[class="btn btn-primary sign-up-btn g-recaptcha"]'
    error_scc_path = '[class="input-validation-error"] '
    # sign_up = page.locator(selector=sign_up_xpath)
    sign_up = page.query_selector_all(selector=sign_up_xpath)
    sign_up[0].click()
    email = page.query_selector(selector=email_scc_path)
    email.fill('anahitaleqs89@gmail.com')
    username = page.query_selector(selector=username_scc_path)
    username.fill("Analeqs")
    password = page.query_selector(selector=password_scc_path)
    password.fill("Ashun2024@")
    free_account = page.query_selector(selector=free_account_scc_path)
    free_account.click()
    error_text = page.query_selector(error_scc_path)
    error_text.is_visible()

    print(error_text.text_content())


    # page.wait_for_timeout(150000000)

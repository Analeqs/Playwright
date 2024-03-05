from playwright.sync_api import Page, expect
from time import perf_counter


def test_wait(page: Page):
    start = perf_counter()
    # page.goto(url="https://www.postman.com/", wait_until="load") # 3.28
    #page.goto(url="https://www.postman.com/", wait_until="commit") # 1.38
    #page.goto(url="https://www.postman.com/", wait_until="domcontentloaded") # 1.54
    #page.goto(url="https://www.postman.com/", wait_until="networkidle") # 30 sec more
    page.goto(url="https://www.postman.com/") # 30 sec more
    # xpath = '//*[text()="Explore the Public API Network →"]'
    # link = page.get_by_role('link', name="Explore the Public API Network →", exact=True)

    sign_up_xpath = '//*[text()="Sign Up for Free"]'
    email_scc_path = 'input[id="email"]'
    # username_scc_path = 'input[id="username"]'
    # password_scc_path = 'input[id="password"]'
    # free_account_scc_path = '[class="btn btn-primary sign-up-btn g-recaptcha"]'
    # error_scc_path = '[class="input-validation-error"] '
    # # sign_up = page.locator(selector=sign_up_xpath)
    sign_up = page.query_selector_all(selector=sign_up_xpath)
    sign_up[0].click(timeout=1000)
    email = page.query_selector(selector=email_scc_path)
    email.fill('anahitaleqs89@gmail.com')



    #time_took = perf_counter()-start
    #print(round(time_took, 2))

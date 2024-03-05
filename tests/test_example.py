from playwright.sync_api import Page, expect
def test_has_title(page: Page):
    page.goto(url="https://www.youtube.com")
    expect(page).to_have_title("YouTube")
    search_element=page.locator('[name="search_query"]')
    search_element.click()
    search_element.fill("Sirusho")
    search_element.press("Enter")

    print(" After enter")


    page.wait_for_timeout(150000000)





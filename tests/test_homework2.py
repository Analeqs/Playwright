from playwright.sync_api import Page, expect


def test_register(page: Page):
    page.goto(url="https://playwright.dev/python")
    search_button_xpath = '//*[text()="Search"]'
    search_input_scc_path = 'input[id="docsearch-input"]'
    screenshots_scc_path = '[class*="DocSearch-Hit-title"]'
    full_page_screenshots_scc_path = 'h2[class="anchor anchorWithStickyNavbar_LWe7"]'
    search_button = page.query_selector(selector=search_button_xpath)
    search_button.click()
    search_input = page.query_selector(selector=search_input_scc_path)
    search_input.fill("screenshots")
    screenshots_element = page.query_selector(selector=screenshots_scc_path)
    screenshots_element.click()
    full_page_screenshots = page.query_selector(selector=full_page_screenshots_scc_path)
    assert full_page_screenshots
    print(full_page_screenshots.text_content())

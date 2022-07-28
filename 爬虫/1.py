from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()

    # Open new page
    page = context.new_page()

    # Go to https://www.baidu.com/
    page.goto("https://www.baidu.com/")

    # Click text=0中国与印尼携手传递哪些信息
    with page.expect_popup() as popup_info:
        page.locator("text=0中国与印尼携手传递哪些信息").click()
    page1 = popup_info.value

    # Click [aria-label="标题：中国与印尼携手传递哪些信息"] >> text=中国与印尼携手传递哪些信息
    with page1.expect_popup() as popup_info:
        page1.locator("[aria-label=\"标题：中国与印尼携手传递哪些信息\"] >> text=中国与印尼携手传递哪些信息").click()
    page2 = popup_info.value
    page1.wait_for_url("https://baijiahao.baidu.com/s?id=1739478906030762537")

    # Click .index-module_videoIcon_FJR9W >> nth=0
    page2.locator(".index-module_videoIcon_FJR9W").first.click()

    # Click .index-module_videoIcon_FJR9W
    page2.locator(".index-module_videoIcon_FJR9W").click()

    # Close page
    page2.close()

    # Close page
    page1.close()

    # Close page
    page.close()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

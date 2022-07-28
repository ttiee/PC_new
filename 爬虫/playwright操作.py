# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/7/28 15:18
作者：神奇

功能:
运行条件:安装playwright

# 安装playwright库
pip install playwright

# 安装浏览器驱动文件（安装过程稍微有点慢）
python -m playwright install

https://www.jb51.net/article/203510.htm


python -m playwright codegen --target python -o 1.py -b cr https://www.baidu.com
"""
from playwright.sync_api import sync_playwright


def run(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.newContext()

    # Open new page
    page = context.newPage()

    page.goto("https://www.baidu.com/")

    page.click("input[name=\"wd\"]")

    page.fill("input[name=\"wd\"]", "jingdong")

    page.click("text=\"京东\"")

    # Click //a[normalize-space(.)='京东JD.COM官网 多快好省 只为品质生活']
    with page.expect_navigation():
        with page.expect_popup() as popup_info:
            page.click("//a[normalize-space(.)='京东JD.COM官网 多快好省 只为品质生活']")
        page1 = popup_info.value
    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
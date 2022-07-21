# -*- coding: UTF-8 -*-

"""
序号:037
功能:自动下载小说
运行条件:安装requests和pyquery库
time=2022/01/27
author=奕凌天
"""

from pyquery import PyQuery as pq
import requests
import time
import re


def get_a_html(number):
    url = 'http://www.bookshuku.com/xuanhuan/index_{}.html'.format(number)
    response = requests.get(url)
    response.encoding = "utf-8"
    html = response.text
    return html


def get_a_href_title(html):
    doc = pq(html)  # 获取网页源码的节点
    a = doc('.mainSoftName a')  # 找到mainListName后面的a节点

    txt_title = []  # 保存书名的列表
    txt_url = []  # 保存书本的链接

    for item in a.items():
        href1 = item.attr('href')  # 获取节点属性---书本查看界面
        # http://www.bookshuku.com/bookinfo/77994.html
        # http://txt.bookshuku.com/home/down/txt/id/77994
        list = re.findall(r'\d+', href1)  # 将书本查看界面链接的数字提取数来
        number = list[0]
        href = 'http://txt.bookshuku.com/home/down/txt/id/' + number  # 书本查看界面到书本下载界面的链接转换

        title = item.text()  # 获取节点文本---书名

        txt_url.append(href)
        txt_title.append(title)

    txt = dict(zip(txt_title, txt_url))  # 将书名和链接组成字典
    return txt


def get_more_href_title():
    page_start = int(input("请输入下载起始页:"))
    page_end = int(input("请输入下载结束页:"))
    txt = dict()

    for i in range(page_start, page_end + 1):
        html = get_a_html(i)
        txt1 = get_a_href_title(html)

        txt.update(txt1)  # 将字典txt1添加到字典txt中
        time.sleep(5)

    return txt


def txt_down():
    txt = get_more_href_title()
    for title, url in txt.items():
        filename = r"./novel/" + title + ".txt"
        f = requests.get(url)

        print("=" * 15 + "开始下载小说", title + "=" * 15)

        with open(filename, "wb") as txt:
            txt.write(f.content)

        print("=" * 15 + "小说", title + "下载完成" + "=" * 15 + "\n\n")
        time.sleep(2)

    print("=" * 18 + "下载完成" + "=" * 18)
    return txt


if __name__ == "__main__":
    txt = txt_down()

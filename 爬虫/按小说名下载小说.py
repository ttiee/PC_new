# -*- coding: UTF-8 -*-

"""
序号:001
功能:自动下载小说_按照书名
运行条件:安装requests和lxml库
time=2022/07/06
author=奕凌天
"""

from lxml import etree
import requests
import re
import datetime

cmd = input("小说名|文件夹名:")

txt_title = cmd.split('|')[0]
folder_name = cmd.split('|')[1]

print("txt_title", txt_title)
print("folder_name", folder_name)

url = 'http://www.bookshuku.com/search.html'

xiaoshuo = {'searchkey': txt_title}
print("xiaoshuo", xiaoshuo)
response = requests.get(url, xiaoshuo)
response.encoding = "utf-8"
html = response.text
et = etree.HTML(html)  # 网页源代码初始化，构造XPath解析对象，同时修正HTML文本
href = et.xpath("//*[@class='searchTopic']/a/@href")[0]
title = et.xpath("//*[@class='searchTopic']/a/@title")[0]

if title == txt_title:
    number = re.findall(r'\d+', href)[0]  # 将书本查看界面链接的数字提取数来
    href = 'http://txt.bookshuku.com/home/down/txt/id/' + number  # 书本查看界面到书本下载界面的链接转换
    filename = r"D:/WorkSpace/PC/机器人/None_QQ/AI/none_qq/novel/" + title + ".txt"
    print("已经找到小说，正在爬取", datetime.datetime.now())
    f = requests.get(href)
    with open(filename, "wb") as txt:
        txt.write(f.content)
    print("已经写完了", datetime.datetime.now())

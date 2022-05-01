from lxml import etree
import requests
import datetime
import re
import json


# 传递一个链接，得到网页源代码
def get_a_html(url):  # 传入url参数，获取网页源代码
    # 创建一个请求头，模拟浏览器
    headers = {'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
    reponese = requests.get(url=url, headers=headers)  # 发起请求，获取响应
    # reponese.encoding = "utf-8"                                    # 响应编译方式配置为utf-8
    html = reponese.text  # 从响应中获取网页源代码
    return html  # 将网页源代码返回给函数


if __name__ == "__main__":
    url3 = 'https://sou-yun.cn/Query.aspx?type=poem1&id=265871'
    res = get_a_html(url3)
    html3 = etree.HTML(res)

    yuanci_name = html3.xpath('//div[@class="poemSentence"]//span[@class="bold"]/text()')

    yuanci_id0 = html3.xpath('//div[@class="poemSentence"]//span[@class="wordLink"]/@onclick')
    yuanci_id = list(map(lambda x: re.findall('\d+', x)[0], yuanci_id0))
    print(yuanci_name)
    print(yuanci_id0)
    print(yuanci_id)

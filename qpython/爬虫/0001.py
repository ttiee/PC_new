# -*- coding: utf-8 -*-
# 爬虫：通过编写程序获取互联网上的资源
# python可实现
# 导入urlopen 模块
from urllib.request import urlopen

url = 'http://www.baidu.com/'
resp = urlopen(url)
res = resp.read().decode('utf-8')
print(res)
# 读取网页内容


with open('mybaidu.html', 'w', encoding='utf-8') as f:
    f.write(res)  # 读取网页的页面源代码
print('over')

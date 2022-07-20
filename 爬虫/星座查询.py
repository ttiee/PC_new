# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd={}是什么星座&oq=%25E7%2594%259F%25E6%2597%25A5%25E6%259F%25A5%25E8%25AF%25A2%25E6%2598%259F%25E5%25BA%25A7%25E7%259A%2584api&rsv_pq=fc3c937200022710&rsv_t=4733Bk3jnaHr8uB1MhMn2GPE2dSqaGlAczstLBNwFb8ZXKMgHhmUfMo1FMc&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_btype=t&inputT=3585&rsv_sug3=35&rsv_sug1=36&rsv_sug7=100&bs=%E7%94%9F%E6%97%A5%E6%9F%A5%E8%AF%A2%E6%98%9F%E5%BA%A7%E7%9A%84api
import requests
import re


url = f'http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&tn=baidu&wd={input("请输入生日：")}是什么星座&oq=%25E7%2594%259F%25E6%2597%25A5%25E6%259F%25A5%25E8%25AF%25A2%25E6%2598%259F%25E5%25BA%25A7%25E7%259A%2584api&rsv_pq=fc3c937200022710&rsv_t=4733Bk3jnaHr8uB1MhMn2GPE2dSqaGlAczstLBNwFb8ZXKMgHhmUfMo1FMc&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_btype=t&inputT=3585&rsv_sug3=35&rsv_sug1=36&rsv_sug7=100&bs=%E7%94%9F%E6%97%A5%E6%9F%A5%E8%AF%A2%E6%98%9F%E5%BA%A7%E7%9A%84api'

res = requests.get(url=url).text

data = re.findall('"sourcename":"百度百科","summary":"(.*?)","', res)[0]
print(data)

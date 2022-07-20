# https://www.fabiaoqing.com/search/bqb/keyword/666
import requests
import re


def search_emoji(keyword: str = '666') -> tuple:
    url = f'https://www.fabiaoqing.com/search/bqb/keyword/{keyword}'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
    }
    res = requests.get(url=url, headers=headers).text
    emoji_url_list = re.findall('data-original="(.*?\.gif)" src="', res)
    emoji_url = tuple(emoji_url_list)
    return emoji_url


for i in search_emoji(input('请输入想要的表情：')):
    print(i)

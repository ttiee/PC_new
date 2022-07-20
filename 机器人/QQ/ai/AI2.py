import requests
import re


# http://api.ruyi.ai/v1/message?q=%E6%97%A9%E5%AE%89&app_key=b2965660-89b4-4900-bec8-5a02070a7701&user_id=123456
# http://api.ruyi.ai/v1/message?q=%E4%BD%A0%E5%8F%AB%E4%BB%80%E4%B9%88&app_key=b2965660-89b4-4900-bec8-5a02070a7701&user_id=123456
# url = 'http://api.ruyi.ai/v1/message'


def shenqi_ai(msg):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
    }
    url = 'http://api.ruyi.ai/v1/message?q={}&app_key=b2965660-89b4-4900-bec8-5a02070a7701&user_id=123456'.format(msg)

    an = requests.get(url=url, headers=headers).json()
    # print(an)
    answer = an['result']['intents'][0]['outputs'][1]['property']['text']
    print(answer)
    return answer


# while 1:
#     q = input('神奇：')
#     shenqi_ai(q)
#     if 'quit' == q:
#         break
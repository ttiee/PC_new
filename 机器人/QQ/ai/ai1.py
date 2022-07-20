import requests
import re

url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'


def question(qt):
    res = requests.get(url=url.format(qt)).json()
    if res['result'] == 0:
        msg1 = re.sub('\{[a-z0-9]+:[a-z0-9]+}', '', res['content'])
        msg = '天使：' + re.sub('\{br}', '\n', msg1)
        print(msg)
    else:
        pass


while 1:
    q = input('神奇：')
    question(q)
    if 'quit' == q:
        break

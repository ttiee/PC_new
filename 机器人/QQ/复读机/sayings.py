import requests


def sayings():
    res = requests.get(url='https://v1.hitokoto.cn/').json()
    msg = f"{res['hitokoto']}\u000a来自：{res['from']}"
    return msg


if __name__ == '__main__':
    sayings()

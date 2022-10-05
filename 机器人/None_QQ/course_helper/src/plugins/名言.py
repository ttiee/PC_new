from nonebot import on_keyword
import requests

t1 = on_keyword({'名言'}, priority=20)


@t1.handle()
async def main():
    res = requests.get(url='https://v1.hitokoto.cn/').json()
    msg = f"{res['hitokoto']}\u000a——来自：{res['from']}"
    await t1.finish(msg)



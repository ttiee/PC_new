from nonebot.adapters.cqhttp import Message
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
import requests
import random

picture = on_keyword({"图片"})

@picture.handle()
async def send_emoji(bot: Bot, event: Event, state: T_State):
    img_url = await get_random_img()
    msg = f"[CQ:image,file={img_url},type=show,id=40004]"
    await get_random_img()
    await picture.send(Message(msg))

async def get_random_img():
    API_URL = 'https://api.r10086.com/王者荣耀.php'
    data = requests.get(API_URL)
    return data.url

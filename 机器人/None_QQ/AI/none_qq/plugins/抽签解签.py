import json

import requests
from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event


def get_chou(qq: str):
    url = 'https://api.iyk0.com/gdlq/?msg=抽签&n=' + qq
    r = requests.get(url)
    message = r.text
    print(message)
    return message


CouQ = on_command("抽签", priority=2, block=True)


@CouQ.handle()
async def chouqian_(bot: Bot, event: Event):
    if int(event.get_user_id()) != event.self_id:
        await bot.send(
            event=event,
            message=str(get_chou(str(Event.get_user_id))),
            at_sedner=True
        )


def get_pao(qq: str):
    url = 'https://api.iyk0.com/gdlq/?msg=抛杯&n=' + qq
    r = requests.get(url)
    message = r.text
    print(message)
    return message


PB = on_command("抛杯", priority=2, block=True)


@PB.handle()
async def paobei_(bot: Bot, event: Event):
    if int(event.get_user_id()) != event.self_id:
        await bot.send(
            event=event,
            message=str(get_pao(str(Event.get_user_id))),
            at_sedner=True
        )


def get_jie(qq: str):
    url = 'https://api.iyk0.com/gdlq/?msg=解签&n=' + qq
    r = requests.get(url)
    result = json.loads(r.content)
    message = str(result['title'] + '\n' + result['desc'])
    print(message)
    return message


JQ = on_command("解签", priority=2, block=True)


@JQ.handle()
async def JQ_(bot: Bot, event: Event):
    if int(event.get_user_id()) != event.self_id:
        await bot.send(
            event=event,
            message=str(get_jie(str(Event.get_user_id))),
            at_sedner=True
        )

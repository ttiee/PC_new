# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/7/27 22:29
作者：神奇

功能:
运行条件:安装
"""
from nonebot import on_message
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Event
t1 = on_message(rule=to_me(), priority=200)
@t1.handle()
async def main(event: Event):
    msg = event.get_message()
    await t1.finish(msg)

# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/11/1 9:48
作者：神奇

功能:
运行条件:
"""
from nonebot import on_keyword
from nonebot.adapters.onebot.v11 import Message

fy = on_keyword({'语音'})


@fy.handle()
async def sj():
    mus5 = r'[CQ:record,file=file:/D:/WorkSpacebot/yuyinbao/你好.mp3]'
    msg = Message(mus5)

    await fy.send(message=msg)

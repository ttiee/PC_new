# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/10/5 14:13
作者：神奇

功能:
运行条件:安装manimgl
"""

from nonebot import on_startswith, on_command, require, on_regex
from nonebot.adapters.onebot.v11 import (
    GROUP,
    GroupMessageEvent,
    MessageSegment,
    Message,
    Bot
)

xww_timetable = on_regex("xww课表.jpg", permission=GROUP, priority=5, block=False)


@xww_timetable.handle()
async def sent_img(bot: Bot, event: GroupMessageEvent):
    img = r'file:///D:/WorkSpace/PC/机器人/None_QQ/course_helper/data/课表.jpg'
    img = MessageSegment.image(file=img)
    await xww_timetable.send(message=Message(img))


qhy_imgs = on_regex("qhy.jpg", permission=GROUP, priority=5, block=False)


@qhy_imgs.handle()
async def sent_img(bot: Bot, event: GroupMessageEvent):
    img1 = r'file:///D:\WorkSpace\PC\机器人\None_QQ\course_helper\data\qhy\a.png'
    img1 = MessageSegment.image(file=img1)
    img2 = r'file:///D:\WorkSpace\PC\机器人\None_QQ\course_helper\data\qhy\b.png'
    img2 = MessageSegment.image(file=img2)
    img3 = r'file:///D:\WorkSpace\PC\机器人\None_QQ\course_helper\data\qhy\c.png'
    img3 = MessageSegment.image(file=img3)
    img4 = r'file:///D:\WorkSpace\PC\机器人\None_QQ\course_helper\data\qhy\d.png'
    img4 = MessageSegment.image(file=img4)

    await qhy_imgs.send(message=Message(f'{img1}\n{img2}\n{img3}\n{img4}'))


lei_liu_jpg = on_regex("禁言大礼包.jpg", permission=GROUP, priority=5, block=False)


@lei_liu_jpg.handle()
async def sent_img(bot: Bot, event: GroupMessageEvent):
    img = r'file:///D:\WorkSpace\PC\机器人\None_QQ\course_helper\data\python_g\禁言大礼包.jpg'
    img = MessageSegment.image(file=img)
    await lei_liu_jpg.send(message=Message(img))


cyh_imgs = on_regex("cyh.jpg", permission=GROUP, priority=5, block=False)


@cyh_imgs.handle()
async def sent_img(bot: Bot, event: GroupMessageEvent):
    img1 = r'file:///D:\WorkSpace\PC\机器人\None_QQ\course_helper\data\cyh\a.jpg'
    img1 = MessageSegment.image(file=img1)
    img2 = r'file:///D:\WorkSpace\PC\机器人\None_QQ\course_helper\data\cyh\b.jpg'
    img2 = MessageSegment.image(file=img2)

    await cyh_imgs.send(message=Message(f'{img1}\n{img2}'))
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message, MessageSegment, Event
from random import choice, randint

fy = on_keyword({'音乐', '语音'})


@fy.handle()
async def sj(bot: Bot, event: Event):
    # msg = MessageSegment('[CQ:record,file=http://music.163.com/song/media/outer/url?id=31365604.mp3]')

    _id = [31365604, 449818326, 548252595, 28613172, 27896762, 1873321491, 36990266]
    msg = Message(f"[CQ:record,file=http://music.163.com/song/media/outer/url?id={choice(_id)}.mp3]")

    await fy.send(message=msg)

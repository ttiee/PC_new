from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message, MessageSegment, Event
import random

fy = on_keyword({'语音'})


@fy.handle()
async def sj(bot: Bot, event: Event):
    # msg = MessageSegment('[CQ:record,file=http://music.163.com/song/media/outer/url?id=31365604.mp3]')

    _id = [31365604, 449818326, 548252595, 28613172, 27896762, 1873321491, 36990266]
    msg = Message(f"[CQ:record,file=http://music.163.com/song/media/outer/url?id={_id[random.randint(0, 6)]}.mp3]")

    await fy.send(message=msg)


music = on_keyword({'music', '音乐', '点歌', '听歌'}, priority=100, rule=to_me())


@music.handle()
async def sj(bot: Bot, event: Event):
    msg = "/点歌/qq点歌/网易点歌/酷我点歌/酷狗点歌/咪咕点歌/b站点歌 + 关键词\n示例：/点歌 最伟大的作品"

    await music.send(message=msg)


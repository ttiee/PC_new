from nonebot import on_keyword, on_command
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Bot, Message, MessageSegment, Event
import random

fy = on_keyword({'语音'})


@fy.handle()
async def sj(bot: Bot, event: Event):
    # msg = MessageSegment('[CQ:record,file=http://music.163.com/song/media/outer/url?id=31365604.mp3]')

    _id = [31365604, 449818326, 548252595, 28613172, 27896762, 1873321491, 36990266]
    msg = Message(f"[CQ:record,file=http://music.163.com/song/media/outer/url?id={_id[random.randint(0, 6)]}.mp3]")

    await fy.send(message=msg)


music = on_command('music', aliases={'音乐', '点歌', '听歌'}, priority=100)


@music.handle()
async def sj(bot: Bot, event: Event):
    msg = "点歌，默认为qq点歌，支持qq、网易、酷我、酷狗、咪咕、b站音频区\n"+"点歌/qq点歌/网易点歌/酷我点歌/酷狗点歌/咪咕点歌/b站点歌 + 关键词"

    await music.send(message=msg)


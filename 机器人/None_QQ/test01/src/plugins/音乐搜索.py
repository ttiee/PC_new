# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/8/20 17:09
作者：神奇

功能:
运行条件:安装manimgl
"""
from typing import Tuple
from nonebot import on_regex
from nonebot.adapters.onebot.v11 import Bot, Message, Event


import os
import requests


music = on_regex(r'1 \w+')


@music.handle()
async def main(event: Event, bot: Bot):
    keyword = str(event.get_message()[0]).replace('1 ', '')
    result = search(keyword=keyword)

    if result[0]:
        _id = result[3]
        msg = Message(f"[CQ:record,file=http://music.163.com/song/media/outer/url?id={_id}.mp3]")

        await music.send(message=msg)

    else:
        await music.send(result[1])


def search(keyword: str) -> Tuple[int, str, str, str]:
    url = "https://music.163.com/api/cloudsearch/pc"
    params = {"s": keyword, "type": 1, "offset": 0, "limit": 1}
    result = requests.post(url=url, params=params).json()
    print(result)

    if songs := result["result"]["songs"]:
        music_name = songs[0]['name']
        music_id = songs[0]["id"]
        return 1, f'https://music.163.com/song/media/outer/url?id={music_id}.mp3', music_name, music_id
    return 0, "网易云音乐中找不到相关的歌曲", '', ''


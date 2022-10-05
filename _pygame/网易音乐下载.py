# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/9/9 22:14
作者：神奇

功能:
运行条件:安装request
"""

import requests

id = 1695956


def download_music(music_id: int = id):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'}

    url = f'https://music.163.com/song/media/outer/url?id={music_id}.mp3'
    con = requests.get(url=url, headers=headers).content
    with open(f'{music_id}.mp3', 'wb') as f:
        f.write(con)
    print('\n下载完成！')


download_music(music_id=id)

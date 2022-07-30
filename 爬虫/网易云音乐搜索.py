# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/7/30 7:57
作者：神奇

功能:
运行条件:安装manimgl
"""
from typing import Tuple

import os
import requests


def search(keyword: str) -> Tuple[int, str, str]:
    url = "https://music.163.com/api/cloudsearch/pc"
    params = {"s": keyword, "type": 1, "offset": 0, "limit": 1}
    result = requests.post(url=url, params=params).json()
    print(result)

    if songs := result["result"]["songs"]:
        music_name = songs[0]['name']
        music_id = songs[0]["id"]
        return 1, f'https://music.163.com/song/media/outer/url?id={music_id}.mp3', music_name
    return 0, "网易云音乐中找不到相关的歌曲", ''


def main():
    keyword = input('输入下载的音乐:')
    result = search(keyword=keyword)

    if result[0]:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'}

        file = requests.get(url=result[1], headers=headers).content

        if 'html' not in str(file):
            if not os.path.exists('music'):
                os.mkdir('music')
            os.chdir('music')
            with open(f'{result[2]}.mp3', 'wb') as f:
                f.write(file)
                print('\n[red]下载完成！')
        else:
            print('\n[red]这首歌要付费呢')

    else:
        print(result[1])


if __name__ == '__main__':
    main()

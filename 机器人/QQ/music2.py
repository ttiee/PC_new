# https://music.liuzhijin.cn/   接口
import requests

headers = {
    'Host': '47.112.23.238',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
    'Accept': 'application/json,*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'http://47.112.23.238/',
    'Connection': 'keep-alive',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
    'Origin': 'http://47.112.23.238',
}

msg_str = '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" templateID="1" ' \
          'action="web" brief="" sourceMsgId="0" url="https://qm.qq.com/cgi-bin/qm/qr?k=wyw10nH14NxBzBmM2DZK_bj9y9yX-IJL" flag="0" adverSign="0" ' \
          'multiMsgFlag="0"><item layout="2"><audio cover="{3}" ' \
          'src="https://music.163.com/song/media/outer/url?id={0}.mp3" ' \
          '/><title>{1}</title><summary>『作者』{2}</summary></item><source name="神奇永远的神！" ' \
          'icon="https://python3student.github.io/img/avatar.jpg" ' \
          'url="https://python3student.github.io/img/avatar.jpg" action="app" a_actionData="com.netease.cloudmusic" ' \
          'i_actionData="tencent100495085://" appid="100495085" /></msg>,resid=60] '


def music_search(song):
    url = 'http://47.112.23.238/Music/getMusicList'
    data = {
        'musicName': song,
        'type': 'netease',
        'number': 2
    }
    music = requests.post(url=url, headers=headers, data=data).json()

    # print(music)

    if music['data'] is None:
        msg = '网易云没有搜索到相关音乐[CQ:face,id=189]'
        print(msg)
        return [msg, None, None, None]

    d_music = music['data'][0]
    music_id = d_music['id']
    music_name = d_music['title']
    music_au = d_music['author']
    music_pic = d_music['pic']
    music_url = d_music['url']
    msg = msg_str.format(music_id, music_name, music_au, music_pic)
    print(msg)
    return [msg, music_url, music_name, music_au]

# '伴你成长'    '孤勇者'   '你从未离去'     '森林狂想曲'
# music_search('你可不可以跟我一起看彩虹')

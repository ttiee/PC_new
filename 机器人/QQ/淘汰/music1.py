import requests

url = 'http://music.cyrilstudio.top/search'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'}


def music_search(song):
    data = {
        'keywords': song,
        'limit': '10'
    }
    music = requests.get(url=url, headers=headers, data=data).json()

    if music['result']['songCount'] == 0:
        print('没有找到相关音乐')

    mark = 0
    d_list = []
    for i in music['result']['songs']:
        print(i)
        if i['mark'] >= mark:
            mark = i['mark']
            d_list = [i]
    r_song = d_list[0]
    print(r_song)
    print(r_song['id'])
    print(r_song['name'])
    return


# '伴你成长'    '孤勇者'   '你从未离去'
music_search('你从未离去')

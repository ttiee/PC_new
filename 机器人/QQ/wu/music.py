import requests
import re


def get_id(song):
    url = "http://music.163.com/api/search/pc"
    pyload = {"s": song, "offset": 0, "limit": 1, 'type': 1}
    lrc_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.139 Safari/537.36 '
    }
    response = requests.post(url=url, data=pyload, headers=lrc_headers).json()
    print(response)
    id = response['result']['songs'][0]['id']
    return id

def get__id(song):
    url = "https://music.163.com/#/search/m/?s={}&type=1".format(song)
    headers = {'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.41 Safari/537.36 Edg/101.0.1210.32'}
    response = requests.post(url=url, headers=headers).text
    # all = re.findall("class='text'", response)
    print(response)

def get___id(song):
    url = "http://music.cyrilstudio.top/song/detail"
    pyload = {'ids': 548252595}
    lrc_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/66.0.3359.139 Safari/537.36 '
    }
    response = requests.get(url=url, data=pyload, headers=lrc_headers).json()
    print(response)
get___id('勇往直前')
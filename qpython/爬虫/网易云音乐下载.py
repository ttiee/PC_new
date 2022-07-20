import requests
import time
from bs4 import BeautifulSoup
count = 0
time_start = time.time()



def music():
    url = 'https://music.163.com/discover/toplist?id=19723756'
    # url = ' http://music.163.com/#/discover/toplist?id=3779629'

    headers = {
        'Sec-Fetch-Mode': 'cors',
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.82 Safari/537.36',
        'referer': 'https://music.163.com/'

    }
    data = {
        "params": "+H6D23233AX7 + ZhHr4HqHLeDwi5A9nhbtTqkxhoFC / A9Jf01CuoQpZ + AX7YFx + +W",
        "encSecKey": "0b87f8306db58707587ee170832712c5781f96adc1890048e339977a819f26b86f814"
                     "c91b2bafbb123a35de4da4d16678f1f5ca2af99657b48048a30dad0b18ed14e2f32c23145c6"
                     "e42349af1356287119e7b1157b544f292b212d7014168b22605b83692af7fc5c4fd3395c86fa7ea9395b4b9fb560b83268044be825c61723"
    }
    response = requests.get(url=url,headers=headers,params=False,data=data).content.decode("utf-8")

    s = BeautifulSoup(response, 'lxml')
    main = s.find('ul', {'class': 'f-hide'})
    list= main.find_all("a")



    for i in list:

        name = i.text.replace("/"," ")
        music_url = 'http://music.163.com/song/media/outer/url' + i['href'][5:] + '.mp3'
        response = requests.get(music_url, headers=headers, allow_redirects=False, data=data)
        url = response.headers.get('Location')

        music = requests.get(music_url,headers=headers,data=data).content
        with open('F:/桌面/Muisc/'+name + '.mp3', mode='wb') as file:
            file.write(music)


        print(music_url,name + "下载成功")
        # (time_end) = time.time()  # 获取结束时间
        # print('下载完成，耗时:' +str(time_end - time_start) + "秒")

    input("任务结束按任意键继续")

if __name__ == '__main__':
    music()



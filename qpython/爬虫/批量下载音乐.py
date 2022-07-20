import requests
import re



# url = "https://music.163.com/discover/toplist?id=3778678"   #网易云网址,以热歌榜单链接为例
url = "https://music.163.com/discover/toplist?id=19723756"
r = requests.get(url)
#二、解析热歌榜歌曲ID、歌曲名字**
#print(r.text)
#<li><a href="/song?id=1901371647">孤勇者</a></li>
id_name = re.findall('<li><a href="/song\?id=(.*?)">(.*?)</a></li>',r.text)
#print(id_name)     #打印查看网易云歌曲ID、歌曲名字


for data in id_name:
    music_id = data[0]
    music_name = data[1]
    print(music_name)
    music_url = "http://music.163.com/song/media/outer/url?id=" + music_id
    print(music_url)
    music_data = requests.get(music_url,timeout=2).content
    with open("F:\桌面\音乐.mp3",'wb') as f:
        f.write(music_data)

    print("下载完成！")


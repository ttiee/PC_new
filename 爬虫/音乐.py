import re

import requests
name = input('歌名：')
url = 'https://music.cyrilstudio.top/search?keywords='+name
a =requests.get(url)
a.encoding='utf-8'
print(re.findall('id":(\d+.)',a.text)[0][0:-1])
print(re.findall('id":(\d+.)',a.text))

Data = requests.get('http://music.163.com/song/media/outer/url?id='+re.findall('id":(\d+.)',a.text)[0][0:-1]+'.mp3').content
with open(name+'.mp3',mode='wb') as f:
    f.write(Data)
print('Ok')
# http://music.163.com/song/media/outer/url?id=1695956.mp3
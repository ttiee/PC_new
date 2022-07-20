import requests
import re


headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'
}
url = 'http://121.5.255.53:5002/'
res = requests.get(url=url, headers=headers).text.replace('\n', '^').replace('\t', '').replace(' ', '')
print(res)

b_list = re.findall('<tr><thscope="row">(.+)</td></tr>', res)
for b in b_list:
    print(b)
    print('\n'*2)

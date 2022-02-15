import requests

res = requests.get('https://m.bilibili.com/ranking/36').text

#print(res)

with open("05.html","w") as f:
	f.write(res)

print("OK!")


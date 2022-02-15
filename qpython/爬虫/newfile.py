import requests

res = requests.get('https://s1.hdslb.com/bfs/static/mult/images/app_logo.png@152w_152h.png').content

#print(res)

with open("02.png","wb") as f:
	f.write(res)
print("OK!")

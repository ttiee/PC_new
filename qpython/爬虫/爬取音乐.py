import requests


url="https://m801.music.126.net/20220321092422/55ece9a5263456dd" \
	"fd775b9e23060773/jdyyaac/545c/045b/025f/c644ded25f31a88f4c35550788c3ed9b.m4a"
data=requests.get(url).content


with open(r"F:\桌面\音乐\张杰.m4a","wb") as f:
	f.write(data)
print("恭喜下载成功")
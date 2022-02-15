import requests

res = requests.get('http://liferestart.syaro.io/public/index.html').text

#print(res)

with open("07.html","w") as f:
	f.write(res)

print("OK!")

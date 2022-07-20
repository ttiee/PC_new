import requests
import json
import time


url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
}
res = requests.get(url=url, headers=headers).json()

# with open('day_ek_data.json', 'w', encoding='utf-8') as f:
#     json.dump(res, fp=f, ensure_ascii=False, indent=4)

mag_list = []
place_list = []
time_list = []
for i in res['features'][::-1]:

    mag_list.append(i['properties']['mag'])
    place_list.append(i['properties']['place'])
    time_data = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(float(str(i['properties']['time'])[0:10])))
    time_list.append(time_data)


print(mag_list)
print(place_list)
print(time_list)

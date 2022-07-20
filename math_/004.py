import re


num = 0
with open('000.txt', 'r', encoding='utf-8') as f:
    all = f.readlines()

for i in all:
    num += int(str(re.findall('(\d*)天兑换第', i)[0]))
    print(num)


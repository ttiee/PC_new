import re

with open('01.html') as f:
    all = f.read()

all = all.lstrip()
all = all.split('"')

meet = []

for i in all:
    if i.startswith('//'):
    	i = 'http:'+i
    	meet.append(i)
    
    if i.startswith('http'):
        meet.append(i)

for n in meet:
    print(n)

with open('01web.txt','w') as f:
	for n in meet:
		f.write(n+'\n')
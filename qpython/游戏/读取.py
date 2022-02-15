import time


n = ['h','hh','hhh','hhhh','hhhhh','hhhhhh','hhhhhhh']
for i in n:
	print(i+'\r',end='')
	time.sleep(0.5)
print(n[6].replace('h','0')+'\r',end='')

def a(i):
	if '\n' in i:
		i = i[:len(i)-1]
	#	print(i,end='')
		#time.sleep(0.1)
		return i
	else:
		return i

with open('/storage/emulated/0/qpython/爬虫/01.html','r') as f:
	all = f.readlines()
	for i in all:
		b = all.index(i)
		i = a(i)
		all[b] = i


#print(all)
for i in all:
	print(i+'\r',end='')
	time.sleep(0.1)

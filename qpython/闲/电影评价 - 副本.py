import re

def n():
	b = input('请输入对这个电影的评价:')
	if not re.match(r'[1-9]$',str(b)):
		print('\n请输入1-9的数字!\n\n'+'='*15+'电影评价'+'='*15)
		return n()
	a = int(b)
	print('你对这个电影的评价是:','☆'*a)

n()
print("\n您已经评价完成(●—●)")

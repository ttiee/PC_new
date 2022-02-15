import re
import 重开2
import chen


def a():
	b = input('what?    1() or 2()\n')
	if not re.match('(1|2)$', b):
		print('again!')
		return a()
	if b == '1':
		重开2.main()
	else:
		#return chen.main()


if __name__ =='__main__':
	a()
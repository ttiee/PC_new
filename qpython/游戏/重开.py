import time
import random
import re
import math


sj = ['也死了','你的家乡发大水，今年收成不好','你的家长很注重你的学习，你也非常努力','你意外伤了人，赔付了很多医疗费','你的父母第一次打你','你的绘画天赋不错','听说日本轰炸了东京','中国一跃成为GDP第一强国','中国收复了日本','你凭借一幅画，在你居住的地方初露锋芒','你的家庭闹了矛盾一直说要离婚','你捡到了一张彩票，中了五百万','你生病了','你开始喜欢阅读','你患上了抑郁症，你的家人都很着急','外界传闻张三在赶着高考时被突如其来的车辆吓出心脏病，死亡了']


def a1():
	'''初始的属性选择'''
	global z1,z2,z3,z4
	print('\n'+'='*20+'属性选择'+'='*20)
	print('属性点为1-10哦')
	zl = "智力:\t"
	tl = "体力:\t"
	yz = "颜值:\t"
	jj = "家境:\t"
	z1 = input("请输入智力属性点：")
	z2 = input("请输入体力属性点：")
	z3 = input("请输入颜值属性点：")
	z4 = input("请输入家境属性点：")
	for i in (z1,z2,z3,z4):
		if not re.match(r'[1-9]$|10$',i):
			print('请输入1到10的数字')
			return a1()
	z1 = int(z1)
	z2 = int(z2)
	z3 = int(z3)
	z4 = int(z4)
	print('='*20+'开始'+'='*20)


def a2():
    '''性别随机选择'''
    wm=("男孩","女孩")							  
    wm1=random.randint(0,1)
    time.sleep(0.5)
    print("你出生了，是个"+wm[wm1])
    time.sleep(0.5)


def a3():
	'''城市农村选择'''
	global z4
	n = random.randint(1,z4)
	if z4 >= 9:
		print('你从小生活在城市')
	else:
		if n < 3:
			print('你从小生活在农村')
		else:
			print('你从小生活在城市')


def a4():
	'''人生过程主程序'''
	global z1,z2,z3,z4
	for age in range(1,101):
		n = random.randint(1,15)
		if age <= 10:
			num = int((z1+z2+z3+z4+70)*2)
		elif age > 10 and age <= 20:
			num = int((z1+z2+z3+z4+50)*2)
		elif age >= 90:
			num = int(z1+z2+z3+z4)
		elif age > 20 and age <= 40:
			num = int(z1+z2+z3+z4+50)
		else:
			num = int((z1+z2+z3+z4)*2+40-age)
		death = random.randint(0,num)
		if  death == 0:
			print("你的生命走到了尽头")
			break
		if age == 100:
			print("你"+str(age)+"岁了!")
			print('你太幸运了!\n你怎么能活那么长时间？\n好吧，你赢了\n( \'ω\' )Win！')
			break
		print("你"+str(age)+"岁了"+","+sj[n])
		time.sleep(0.1)
	return age - 1


def a5(a):
	'''人生评价'''
	print('='*20+'人生评价'+'='*20+'\n你总共活了{}岁'.format(a),end='，')
	if a <= 20:
		print('属于是夭折了。')
	elif a > 20 and a <= 30:
		print('英年早逝啊！')
	elif a > 30 and a <= 50:
		print('正是建功立业的时候啊。')
	elif a > 50 and a <= 70:
		print('希望下次活的更久一点')
	elif a > 70 and a <= 90:
		print('寿命挺长啊！')
	elif a > 90 and a < 100:
		print('确实厉害(✪▽✪)')
	else:
		pass
	print('='*20+'人生结束'+'='*20)


def a6():
	'''轮回程序'''
	b = input('还想重开吗?  1(想) or 2(不想)\n')
	if not re.match(r'(1|2)$',b):
		print('请输入1或2!')
		return a6()
	if b == '1':
		main()


def main():
	'''设置主循环'''
	a1()
	a2()
	a3()
	age = a4()
	a5(age)
	a6()


if __name__ == '__main__':
	main()
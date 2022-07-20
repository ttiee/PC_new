# _*_coding=UTF-8_*_
import time
import random
import re
import math

sc = ['也死了', '你的家乡发大水，今年收成不好', '你意外伤了人，赔付了很多医疗费', '听说日本轰炸了东京', '中国一跃成为GDP第一强国', '中国收复了日本', '你的家庭闹了矛盾一直说要离婚',
      '你捡到了一张彩票，中了五百万', '你生病了']

# 学前经历
sc0 = ['你的识字量达到了300', '你父母并没有精心照顾你', '你的父母第一次打你', '你的家人为你制定了长长的人生计划', '家里的茅坑废弃了，换成了马桶']

# 幼儿园经历
sc1 = ['你听到一个轮回转世的神话故事。\n你感觉似曾相识', '你开始喜欢阅读', '你凭借一幅画，在你居住的地方初露锋芒', '你喜欢用父母的手机刷抖音', '你的奶奶因病去世了，你很伤心']

# 小学经历
sc2 = ['你不小心摔掉一个门牙', '你的家长很注重你的学习，你也非常努力', '外界传闻张三在赶着高考时被突如其来的车辆吓出心脏病，死亡了', '你们班主任为了生三胎辞职了', '你家养了一只猫', '你们的体育课总是变成自习课']

# 中学经历
sc3 = ['你和几个同学打了架', '你有几次考试考的不太好', '你在回家的路上捡到几块钱,非常开心', '你第一次当上了课代表']

# 高中经历
sc4 = ['你和一个老师闹了很大的矛盾，心情非常不好(╥ω╥`)', '你患上了抑郁症，你的家人都很着急', '外界传闻张三在赶着高考时被突如其来的车辆吓出心脏病，死亡了', '你爱上了刷B站', '你突然对python感兴趣']

# 修仙经历
sc9 = ['你在闭关中', '你离神仙更近了一步', '你吞下了一个仙丹感觉很有用', '你四处寻师但一无所获']


def begin():
    print('=' * 25 + '初始化中' + '=' * 25 + '\n')
    for i in range(1000):
        print("|" * (i // 50), i / 10, "%\r", end='')
        time.sleep(0.0001)
    print('|' * 20 + '  加载完成  ')


def put():
    '''输入属性的函数，在a1函数中被调用'''
    global At1, At2, At3, At4
    print('属性点为1-10哦')
    At1 = input("请输入智力属性点：")
    At2 = input("请输入体力属性点：")
    At3 = input("请输入颜值属性点：")
    At4 = input("请输入家境属性点：")
    for i in (At1, At2, At3, At4):
        if not re.match(r'[1-9]$|10$', i):
            print('请输入1到10的数字')
            print('\n' + '=' * 25 + '属性选择' + '=' * 25)
            return put()
    At1 = int(At1)
    At2 = int(At2)
    At3 = int(At3)
    At4 = int(At4)
    print('=' * 25 + '人生开始' + '=' * 25)


def a1():
    '''初始的属性选择，包括随机选择和输入选择'''
    global At1, At2, At3, At4
    print('\n' + '=' * 25 + '属性选择' + '=' * 25)
    b = input('随机属性吗(●—●)?	1(随机) or 2(不随机) or 3(一键全满) or 4(神仙模式)\n')
    if not re.match('[1234]$', b):
        print('请输入1,2,3,4其中的一个')
        return a1()
    if b == '1':
        At1 = random.randint(1, 10)
        At2 = random.randint(1, 10)
        At3 = random.randint(1, 10)
        At4 = random.randint(1, 10)
        print('你的智力为:\t{}'.format(At1))
        print('你的体力为:\t{}'.format(At2))
        print('你的颜值为:\t{}'.format(At3))
        print('你的家境为:\t{}'.format(At4))
        print('=' * 25 + '人生开始' + '=' * 25)
        return 0.5
    elif b == '3':
        At1 = 10
        At2 = 10
        At3 = 10
        At4 = 10
        print('你的智力为:\t{}'.format(At1))
        print('你的体力为:\t{}'.format(At2))
        print('你的颜值为:\t{}'.format(At3))
        print('你的家境为:\t{}'.format(At4))
        print('=' * 25 + '人生开始' + '=' * 25)
        return 0.2
    elif b == '4':
        At1 = 100
        At2 = 100
        At3 = 100
        At4 = 100
        print('你的智力为:\t{}'.format(At1))
        print('你的体力为:\t{}'.format(At2))
        print('你的颜值为:\t{}'.format(At3))
        print('你的家境为:\t{}'.format(At4))
        print('=' * 25 + '人生开始' + '=' * 25)
        return 0.02
    else:
        put()
        return 0.5


def a2():
    """性别随机选择"""
    wm = ("男孩", "女孩")
    wm1 = random.randint(0, 1)
    time.sleep(0.5)
    print("你出生了，是个" + wm[wm1])
    time.sleep(0.5)


def a3():
    """出生地随机选择"""
    global At4
    n = random.randint(1, At4)
    if At4 >= 9:
        print('你从小生活在城市')
    else:
        if n < 3:
            print('你从小生活在农村')
        else:
            print('你从小生活在城市')
    time.sleep(0.5)


def a4(t):
    """人生过程主程序"""
    s = sc[:]
    s0 = sc0[:]
    s1 = sc1[:]
    s2 = sc2[:]
    s3 = sc3[:]
    s9 = sc9[:]
    global At1, At2, At3, At4
    for age in range(1, 1501):
        if age <= 10:
            num = int((At1 + At2 + At3 + At4 + 70) * 2)
        elif 10 < age <= 20:
            num = int((At1 + At2 + At3 + At4 + 50) * 2)
        elif age >= 90:
            num = int(At1 + At2 + At3 + At4)
        elif age > 20 and age <= 40:
            num = int(At1 + At2 + At3 + At4 + 50)
        else:
            num = int((At1 + At2 + At3 + At4) * 2 + 40 - age)
        death = random.randint(0, num)
        if death == 0:
            print("你的生命走到了尽头")
            break
        if age == 100:
            print("你" + str(age) + "岁了!")
            print('你太牛了!')
            continue
        elif age == 18:
            print("你18岁了，你成年了")
            continue
        elif age == 4:
            print("你4岁了，你上幼儿园了")
            continue
        elif age == 7:
            print("你7岁了，你上小学了")
            continue
        elif age == 13:
            print("你13岁了，你上中学了")
        elif age == 16:
            print("你16岁了，你中考考的并不太好，你上了一个普通的高中了")
        elif age == 200:
            print('你200岁了，你开始想修仙')
        elif age == 1500:
            print('恭喜你成为了神仙!')
            return age
        elif age > 200:
            n = random.randint(0, len(s9) - 1)
            print("你" + str(age) + "岁了" + "," + s9[n])
        elif age < 4:
            n = random.randint(0, len(s0) - 1)
            print("你" + str(age) + "岁了" + "," + s0[n])
            s0.remove(s0[n])
        elif 4 < age < 7:
            n = random.randint(0, len(s1) - 1)
            print("你" + str(age) + "岁了" + "," + s1[n])
            s1.remove(s1[n])
        elif age > 7 and age < 13:
            n = random.randint(0, len(s2) - 1)
            print("你" + str(age) + "岁了" + "," + s2[n])
            s2.remove(s2[n])
        elif age > 13 and age < 16:
            n = random.randint(0, len(s3) - 1)
            print("你" + str(age) + "岁了" + "," + s3[n])
            s3.remove(s3[n])
        else:
            n = random.randint(1, len(s) - 1)
            print("你" + str(age) + "岁了" + "," + s[n])
        time.sleep(t)
    return age - 1


def a5(a):
    '''人生评价'''
    print('=' * 25 + '人生评价' + '=' * 25 + '\n你总共活了{}岁'.format(a), end='，')
    if a <= 20:
        print('属于是夭折了。')
    elif 20 < a <= 30:
        print('英年早逝啊！')
    elif 30 < a <= 50:
        print('正是建功立业的时候啊。')
    elif a > 50 and a <= 70:
        print('希望下次活的更久一点')
    elif a > 70 and a <= 90:
        print('寿命挺长啊！')
    elif a > 90 and a < 100:
        print('确实厉害(✪▽✪)')
    elif 100 <= a < 134:
        print('你简直是人生赢家!\n太厉害了(✪▽✪)!')
    elif a >= 200:
        print('还差一点就成了神仙')
    elif a == 1500:
        print('哇塞，你竟然成了神仙!')
    else:
        print('恭喜你打破了吉尼斯世界纪录')
    print('=' * 25 + '人生结束' + '=' * 25)


def a6():
    """轮回程序"""
    b = input('还想重开吗?  1(想) or 2(不想)\n')
    if not re.match(r'[12]$', b):
        print('请输入1或2!')
        return a6()
    if b == '1':
        main()


def main():
    '''游戏主循环'''
    t = a1()
    a2()
    a3()
    age = a4(t)
    a5(age)
    a6()


if __name__ == '__main__':
    # begin()
    main()

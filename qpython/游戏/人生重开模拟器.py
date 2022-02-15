'''
名称：人生重开模拟器简化版V1.2
制作者：WeChat@鲁迅
参与制作：WeChat@乐乐学
		WeChat@守护星辰的.ikun
V1.0开始制作时间：2022年1月28日
V1.0结束时间：2022年1月29日
V1.2修改时间：2022年1月29日
V1.0介绍：创建了基础功能，但经历不会影响属性，预计在V2.0版本加入可以改变属性的代码
V1.2更新日志：增加了素材库，增加注释
'''
#_*_coding=UTF-8_*_
import random
import time
import datetime
print('现在是'+str(datetime.datetime.now()))

def shuxing():                                      #写入属性的函数
    print("===============选择属性================")
    zl="智力："
    tl="体力："
    yz="颜值："
    jj="家境："
    print("你有10点属性供你选择")
    z1=int(input("请输入智力属性点："))
    z2=int(input("请输入体力属性点："))
    z3=int(input("请输入颜值属性点："))
    z4=int(input("请输入家境属性点："))
    assert (z1+z2+z3+z4)==10,"在这样搞程序就要坏啦"    #控制属性点加成在10点
    print("===============最终选择================")
    print(zl+str(z1))
    print(tl+str(z2))
    print(yz+str(z3))
    print(jj+str(z4))
try:											   #解决由于属性点加成不到或者超过十点的报错
    shuxing()
except AssertionError:
    print("请不要选择高于十点或者没用完十点的属性值，请重新选择")
    shuxing()
print("由于V2.0版本中，属性值会有不同的结局，请再次确认，如果两次不一样，以这次为准")
z1=int(input("请输入智力属性点："))
z2=int(input("请输入体力属性点："))
z3=int(input("请输入颜值属性点："))
z4=int(input("请输入家境属性点："))
print("===============开始你的人生吧===========")
def zhuti():
    wm=("男孩","女孩")							  #随机男女
    wm1=random.randint(0,1)
    time.sleep(0.5)
    print("你出生了，是个"+wm[wm1])
    time.sleep(0.5)
    #======================人生经历素材库=======================
    sj=['也死了','你的家乡发大水，今年收成不好','你的家长很注重你的学习，你也非常努力','你意外伤了人，赔付了很多医疗费','你的父母第一次打你','你的绘画天赋不错','听说日本轰炸了东京','中国一跃成为GDP第一强国','中国收复了日本','你凭借一幅画，在你居住的地方初露锋芒','你的家庭闹了矛盾一直说要离婚','你捡到了一张彩票，中了五百万','你生病了','你开始喜欢阅读','你患上了抑郁症，你的家人都很着急','外界传闻张三在赶着高考时被突如其来的车辆吓出心脏病，死亡了']
    b=15
    for age in range(2,101):                     #年纪 
        a=random.randint(0,b)
        if age==18:
            print("18岁，你成年了")
            continue
        elif age==4:
            print("4岁，你上幼儿园了")
            continue
        elif age==7:
            print("7岁，你上小学了")
            continue
        elif age==13:
            print("13岁，你上中学了")
        elif age==16:
            print("16岁，你上高中了")
        else:
            print("你"+str(age)+"岁了"+","+sj[a])
            #================防止人生经历重复====================
            sj.remove(sj[a])
            if age!=4 or age!=7 or age!=13 or age!=16 or age!=18:
                b=b-1
            else:
                pass
            if a==3:
                global z4
                z4=z4-1
            time.sleep(0.5)
        if  a==0 or b==0:
            print("你的生命走到了尽头")
            break
if z2<2:
    print('体力值不够，您已阵亡')
elif z1<2:
    print('你太傻了，出生就被掐死了')
elif z3>5:
    print("你一出生就把护士帅死了，出生失败")
elif z4<3:
    print("你出生时没有足够的钱，出生失败")
else:
    zhuti()
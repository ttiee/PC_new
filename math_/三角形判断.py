import math


def main():
    l_list = []
    a = int(input('请输入三角形的一边长：'))
    l_list.append(a)
    b = int(input('请输入三角形的一边长：'))
    l_list.append(b)
    c = int(input('请输入三角形的一边长：'))
    l_list.append(c)

    l_list.sort()
    if l_list[0] + l_list[1] <= l_list[2]:
        print('不能构成三角形呢')
        return None
    p = (a + b + c)/2
    S = math.sqrt(p*(p - a)*(p - b)*(p - c))
    print('三角形的面积为：', S)


while 1:
    main()

#!/usr/bin/python3
from fractions import Fraction

num = Fraction(1_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000_0000)

while 1:
    t = []
    x = num
    Count = 0
    limit = 2000  # 位数限制

    while x not in t and Count <= limit - 1 and x != 1:
        t.append(int(x))

        if x % 2 == 0:
            x = x / 2
            # print(num, Count, x)
            Count = Count + 1
        else:
            x = x * 3 + 1
            # print(num, Count, x)
            Count = Count + 1

    if Count != limit:
        # print(t)
        ...
    else:
        print(f'在{limit}的范围内没有收敛')

    z = input(str(num) + ' 过程次数: ' + str(Count))
    num = num + 1

number = int(input('请输入数字：'))
step = 0

print(number, end=' ')


def n(num):
    global step
    if num == 1:
        print(f'步长为：{step}')
    else:
        if num % 2 == 0:
            num = int(num / 2)
            print(num, end=' ')
            step += 1
            return n(num=num)
        else:
            num = 3 * num + 1
            print(num, end=' ')
            step += 1
            return n(num=num)


n(num=number)

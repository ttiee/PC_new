number = int(input("请输入需要分解的数字："))
print(f"{number} =", end=' ')
while number > 1:
    for i in range(2, number + 1):
        if number % i == 0:
            number = int(number / i)
            if number == 1:
                print(i)
            else:
                print(f'{i} *', end=' ')

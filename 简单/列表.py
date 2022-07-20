def sub_1(num_list: list) -> list:
    num1 = str(num_list[0])
    num2 = str(num_list[1])
    if num2 in num1:
        index = num1.index(num2)    # 获取索引
        num1 = num1[:index] + num1[index+1:]    # 拆分重组
    return [num1]


print(sub_1([12454, 3]))

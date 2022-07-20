# num = input("请您为《肖申克的救赎》这部电影打分（只能输入数字1~9）：")
# if num.isdigit():
#     if 1 <= int(num) <= 9:
#         print("您为《肖申克的救赎》电影的评价是", int(num) * "★")
#     else:
#         print("不符合范围，请重新输入")
# else:
#     print("不是整数，请重新输入")

for k, v in str.__dict__.items():
    print(k, '\t\t', v)
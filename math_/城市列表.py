list1 = input("请输入五个城市的名字，用空格分隔：").split(" ")
print('城市列表：', list1)  # (1)
print('循环遍历：')
for n in list1:
    print(n)  # (2)for 循环遍历
print('家乡城市名：', list1[0])  # (3)所在家乡城市名
print('其他城市列表：', list1[1:])  # 其他城市名
d = list1[::-1]
print('反转列表：', d)  # (4)切片法逆序输出
list1.reverse()
print('逆序输出：', list1)
list1.reverse()

# reverse逆序输出
# (5)sort 与 sorted用法
list2 = list1[:]
list2.sort()
print('降序排序（sort）：', list2)
list3 = sorted(list1)
print('降序排序（sorted）：', list3)

list3_index = list3.index(list1[0])
print('降序后的列表前面或后面和家乡的名字：')
if list3_index == len(list3) - 1:  # (6)通过索引找家乡前面，后面的城市,并输出这三个城市
    print(list3[list3_index - 1])
    print(list3[list3_index])
elif list3_index == 0:
    print(list3[list3_index + 1])
    print(list3[list3_index])
else:
    print(list3[list3_index - 1])
    print(list3[list3_index])
    print(list3[list3_index + 1])
print('修改家乡前面，后面的诚市名字：', end='')
if list3_index == len(list3) - 1:  # (7)修改家乡前面，后面的诚市名字，并输出
    list3[list3_index - 1] = 'xj新疆'
    print(list3)
elif list3_index == 0:
    list3[list3_index + 1] = 'xj新疆'
    print(list3)
else:
    list3[list3_index - 1] = 'xj新疆'
    list3[list3_index + 1] = 'ys榆树'
    print(list3)
print('删除家乡前面，后面的诚市名字：', end='')
if list3_index == len(list3) - 1:
    list3.remove(list3[list3_index - 1])  # (8)去除修改家乡名字后的诚市
    print(list3)
elif list3_index == 0:
    list3.remove(list3[list3_index + 1])
    print(list3)
else:
    list3.remove(list3[list3_index - 1])
    print(list3_index)
    list3.remove(list3[list3_index])
    print(list3)

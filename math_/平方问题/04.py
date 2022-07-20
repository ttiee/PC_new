# 先读取出各个数
with open('section.in', 'r') as f:
    line_list = f.readlines()
# print(line_list)
line1 = line_list[0].strip()
line2 = line_list[1]
# print(line1)
# print(line2)
n = int(line1.split(' ')[0])
m = int(line1.split(' ')[1])
# print(n)
# print(m)
all_num_list = line2.split(' ')
for index, item in enumerate(all_num_list):
    all_num_list[index] = int(item)
# print(all_num_list)

# 找出最大平方和
all_sum = 0




print('\n最大平方和为：' + str(all_sum))

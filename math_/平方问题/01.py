# 先读取出各个数
with open('section.in', 'r') as f:
    line_list = f.readlines()
print(line_list)
line1 = line_list[0].strip()
line2 = line_list[1]
print(line1)
print(line2)
n = line1.split(' ')[0]
m = line1.split(' ')[1]
print(n)
print(m)
all_num_list = line2.split(' ')
print(all_num_list)

# 找出最大平方和
the_sum = []
for section_num in range(m):
    for section in range(section_num):
        for n in range(n):
            pass

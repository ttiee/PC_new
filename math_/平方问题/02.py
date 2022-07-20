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

section_lists = []
for i in range(m):
    section_lists.append([])


def get_sum():
    global all_sum
    num_list = all_num_list
    section_list = section_lists
    for s_index, section in enumerate(section_list):
        for n1 in range(n):
            section_list[s_index] = num_list[:n1]
            print(len(num_list))
            # if len(num_list) == 0:

            num_list = num_list[n1 + 1:]
            for d_index, d_section in enumerate(section_list):
                print('区间列表为：', section_list)
                __sum = 0
                if len(d_section) != 0:
                    for num in d_section:
                        __sum += (num + d_index + 1) ** 2
                print('和为：' + str(__sum))
            if __sum >= all_sum:
                all_sum = __sum
        section_list = section_lists
        num_list = all_num_list


    return all_sum


print('\n最大平方和为：' + str(get_sum()))

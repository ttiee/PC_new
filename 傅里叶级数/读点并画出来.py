import turtle as t


with open('dian.txt', 'r') as f:
    point_data_list = f.readlines()
for index, i in enumerate(point_data_list):
    if '\n' in i:
        point_data_list[index] = i.replace('\n', '')
    if '\t' in i:
        point_data_list[index] = i.replace('\t', ' ')

point_data1 = ''.join(point_data_list).replace('\n', '')
# print(point_data1)
point_list = point_data1.split()


def go_point(pointlist: list):
    t.pu()
    for point in pointlist:
        x = float(point.split(',')[0])/5
        y = -float(point.split(',')[1])/5
        t.goto(x=x, y=y)
        t.pd()


go_point(point_list)
t.done()
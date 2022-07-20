a = ('A', 'B', 'C', 'D', 'E', 'F')
b = ('B', 'B', 'A', 'D', 'E', 'E')

ls = []


for k, v in zip(a, b):
    if k != v:
        ls.append(k+v)
    else:
        ls.append(k)

for i in ls:
    for j in ls:
        if i == j:
            continue
        elif set(i) & set(j):
            print(ls, i, j)
            ls.remove(i)
            ls.remove(j)
            ls.append(''.join(set(i) | set(j)))
            # break

print(ls)


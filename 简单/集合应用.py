# %%timeit
lst1 = ["A", "B", "C", "D", "E", "F"]
lst2 = ["B", "B", "A", "D", "E", "E"]

ans = []
for a, b in zip(lst1, lst2):
    for lset in ans:
        if (a in lset) or (b in lset):
            lset.add(b)
            lset.add(a)
            break
    else:
        ans.append({a, b})

for set1 in ans:
    for set2 in ans:
        if set1 == set2:
            continue
        if set1 & set2:  # 有交集
            set1 |= set2  # 更新
            ans.remove(set2)


print(ans)
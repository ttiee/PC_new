money = 35

for i in range(5):
    guess_money = int(input(f'第{i+1}次猜奖品价格:'))
    if guess_money == money:
        print('猜对了！\n奖品带回家')
        break
    if i == 4:
        print(f'五次机会都猜错了，不能把奖品带回家\n\n正确的答案是{money}')
        break
    print(f'猜错了，还有{4-i}次机会\n')

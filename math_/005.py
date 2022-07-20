"""
系统奖励余额10积分，可用这10积分兑换一个12积分的任务卡，分三十天返回，每天返12/30积分，只要余额满足10积分就可以兑换一次12积分的任务卡。
1.请问半年能总共能有多少积分
2.如果有100积分需要多久？
"""


class Main:
    all_day = int(input('天数限制为:'))
    money = 10
    day = 0
    all_card_num = 0
    card_list = []

    def start_main(self):
        while True:

            Main.day += 1
            self.remove_card()
            self.buy_card()
            self.use_cards()
            self.buy_card()
            self.remove_card()
            print('第{}天了，'.format(Main.day) + '当前积分为：{:.1f}，'.format(Main.money) + '当前持有有{}张积分卡，'.format(len(Main.card_list)) + '共兑换了{}张积分卡'.format(Main.all_card_num))
            if len(Main.card_list) == 0:
                break

    def buy_card(self):
        if Main.money >= 10 and (len(Main.card_list) <= 15) and (Main.day <= Main.all_day):
            Main.money -= 10
            card = Card()
            Main.card_list.append(card)
            Main.all_card_num += 1

    def remove_card(self):
        for card in Main.card_list:
            if card.day == 0:
                Main.card_list.remove(card)
                # Main.money += 2  # 奖励2

    def use_cards(self):
        for card in Main.card_list:
            card.use()


class Card:

    def __init__(self):
        self.day = 30

    def use(self):
        Main.money += 0.4
        self.day -= 1


if __name__ == '__main__':
    Main().start_main()

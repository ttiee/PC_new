#!/usr/bin/python3
# *_*coding:utf8 *_*

import card

# 欢迎
card.welcome()
while True:
    # 接受指定
    command = input("请选择操作功能：")
    # 根据指定完成功能
    if command == "1":
        card.new_card()
    elif command == "2":
        card.show_all()
    elif command == "3":
        card.search_card()
    elif command == "0":
        print("退出名片管理系统")
        break
    else:
        print("无效输入")

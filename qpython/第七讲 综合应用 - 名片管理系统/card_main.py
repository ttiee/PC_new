#!/usr/bin/python3

# *_*coding:utf8 *_*
# @Time : 2020/4/23 16:56
# @Author : FengLin
# @Email : damon__dong@163.com
# @File : card_main.py

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

#!/usr/bin/python3

# *_*coding:utf8 *_*
# @Time : 2020/4/23 16:48
# @Author : FengLin
# @Email : damon__dong@163.com
# @File : card.py

"""
名片管理系统
姓名
QQ
电话
"""

card_list = []
# 模块
# 说明文档（提示）

# 函数  封装功能代码块

# 欢迎界面
def welcome():
    print(
        """
        **************************************************
        欢迎使用【名片管理系统】V1.0
    
        1. 新建名片
        2. 显示全部
        3. 查询名片
    
        0. 退出系统
        **************************************************
        """
    )


def new_card():
    print("\n【新建名片】")
    
    name = input("请输入姓名：")
    qq = input("请输入QQ：")
    phone = input("请输入电话：")
    cart = {
        "姓名": name,
        "QQ": qq,
        "电话": phone
    }
    card_list.append(cart)
    print("{} 的名片保存成功".format(name))


def show_all():
    print("\n【显示全部】")
    for card in card_list:
        #print(card)
        for key, value in card.items():
            print(key, ":", value)
    print("\n\n")


def search_card():
    print("\n【查询名片】")
    query_name = input("请查询姓名：")
    # [第1个人， 第2个人]
    for card in card_list:
        if query_name in card.values():
            for key, value in card.items():
                print(key, ":", value)
            break
    else:
        print("没有查询到信息")

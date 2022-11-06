# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/11/5 15:54
作者：神奇

功能:
运行条件:安装manimgl
"""
with open('pi.txt', 'r') as f:
    a = f.read()
with open('pi.txt', 'w') as f:
    f.write(a.replace(' ', ''))

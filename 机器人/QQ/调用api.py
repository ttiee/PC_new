# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/7/31 21:27
作者：神奇

功能:
运行条件:安装manimgl
"""
# -*- coding: utf-8 -*-
import socket

port = 5700


def set_group_whole_ban(resp_dict: {str: int}):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    ip = '127.0.0.1'
    client.connect((ip, port))

    group_id = resp_dict['group_id']  # 群id
    enable = resp_dict['enable']  # True禁言

    payload = f"GET /set_group_whole_ban?group_id={str(group_id)}&enable={enable}" + " HTTP/1.1\r\nHost:" + ip + f":{port}\r\nConnection: close\r\n\r\n "

    print(f"禁言{payload}")
    client.send(payload.encode("utf-8"))
    client.close()
    return None


set_group_whole_ban({'group_id': 757318739, 'enable': True})

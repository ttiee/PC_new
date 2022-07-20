# -*- coding: UTF-8 -*-
import requests


def get_group(id):
    response = requests.post('http://127.0.0.1:5700/get_group_member_list?group_id=' + str(id)).json()
    for i in response['data']:
        if i['card'] != '':
            print(i['card'] + '\t:\t' + str(i['user_id']))
        else:
            print(i['nickname'] + '\t:\t' + str(i['user_id']))



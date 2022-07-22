import requests

from nonebot import on_keyword
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Bot, Event, Message

AI = on_keyword({'AI', 'ai', ''}, rule=to_me(), priority=10)


@AI.handle()
async def say(bot: Bot, event: Event):
    user_id = event.get_user_id()

    # await AI.send(event.get_message())

    if str(event.get_message()) != '退出':
        msg = get_data(str(event.get_message()))
        msg = Message(f'[CQ:at,qq={user_id}]' + msg + '[CQ:face,id=189]')
        await AI.reject(msg)
    else:
        await AI.send(Message(f'[CQ:at,qq={user_id}]退出成功[CQ:face,id=190]'))


def get_data(sya: str) -> str:
    access_token = '24.8ae617c9be3d5810152384b8e47d3be5.2592000.1660661260.282335-26727598'
    url = 'https://aip.baidubce.com/rpc/2.0/unit/service/v3/chat?access_token=' + access_token
    post_data = {
        "version": "3.0",
        "service_id": "S72336",
        "session_id": " ",
        "log_id": "7758521",
        "request": {"terminal_id": "88888",
                    "query": sya}
    }

    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, json=post_data, headers=headers)
    data = response.json()['result']['responses'][0]['actions'][0]['say']

    return data


def shen_qi_ai(msg: str) -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39 '
    }
    url = 'http://api.ruyi.ai/v1/message?q={}&app_key=b2965660-89b4-4900-bec8-5a02070a7701&user_id=123456'.format(msg)

    an = requests.get(url=url, headers=headers).json()
    # print(an)
    answer = an['result']['intents'][0]['outputs'][1]['property']['text']
    print(answer)
    return answer

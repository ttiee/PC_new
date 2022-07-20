import datetime
import json
import random

from nonebot import on_keyword  # http://v2.nonebot.dev
from nonebot.adapters import Event
from nonebot.adapters.onebot.v11 import Bot

an = on_keyword({'签到', '/签到'}, priority=4)


data_path = r'D:\WorkSpace\PC\机器人\None_QQ\AI\data\data.json'


@an.handle()
async def main(event: Event, bot: Bot):

    try:
        with open(data_path, 'r', encoding='utf-8') as f:
            users_dic = json.loads(f.read())
        user_id = event.get_user_id()
        qd_time = str(datetime.date.today())

        user = eval(str(await bot.get_stranger_info(user_id=int(user_id), no_cache=True)))
        user_nick = user['nickname']

        if user_id in users_dic:
            users_score = users_dic[user_id]['score']
            if qd_time == users_dic[user_id]['days'][-1]:
                await an.send(f'今日已经签过到了\u000a当前总积分：{users_score}')
                return None
            else:
                score = random.randint(3, 20)
                if user_nick != users_dic[user_id]['nick'][-1]:
                    users_dic[user_id]['nick'].append(user_nick)
                users_dic[user_id]['score'] += score
                users_dic[user_id]['days'].append(qd_time)

        else:
            score = random.randint(10, 20)
            users_dic[user_id] = {'nick': [], 'score': score, 'days': []}
            users_dic[user_id]['nick'].append(user_nick)
            users_dic[user_id]['score'] = score
            users_dic[user_id]['days'].append(qd_time)

        users_score = users_dic[user_id]['score']

        with open(data_path, 'w', encoding='utf-8') as p:
            p.write(json.dumps(users_dic, indent=4, ensure_ascii=False))

    except ValueError:
        r = False
        await an.send('签到失败')
        with open(data_path, 'r', encoding='utf-8') as f:
            if f.read() == '':
                await an.send(f'数据被清空了{f.read()}，请重新签到')
                await user_data(bot=bot)
                r = True
        if r:
            with open(data_path, 'w', encoding='utf-8') as f:
                f.write('{}')
    else:
        await an.send(f'签到成功\u000a获得积分：{score}\u000a当前总积分：{users_score}')


async def user_data(bot: Bot):
    # bot = get_bot("bot_id")
    result = await bot.get_stranger_info(user_id=1662941153)
    await an.send(str(result))
    # await bot.call_api("get_user_info", user_id=1662941153)

import datetime
import json
import random

from nonebot import on_keyword  # http://v2.nonebot.dev
from nonebot.adapters import Event
from nonebot.adapters.onebot.v11 import Bot, Message


an = on_keyword({'积分', '/积分', '积分查询'}, priority=4)


data_path = r'D:\WorkSpace\PC\None_QQ\qq2\qq2\data\data.json'


@an.handle()
async def main(event: Event, bot: Bot):
    with open(data_path, 'r', encoding='utf-8') as f:
        users_dic = json.loads(f.read())
    user_id = event.get_user_id()
    today = str(datetime.date.today())

    user = eval(str(await bot.get_stranger_info(user_id=int(user_id), no_cache=True)))
    user_nick = user['nickname']
    face = Message('[CQ:face,id=190]')
    k = '\u000a' + face

    if user_id in users_dic:
        qd_time = users_dic[user_id]['days'][-1]
        days = str(len(users_dic[user_id]['days']))

        users_score = str(users_dic[user_id]['score'])
        sort_list = sorted(users_dic.items(), key=lambda x: x[1]['score'], reverse=True)
        pai_hang_dic = {_[0]: str(index + 1) for index, _ in enumerate(sort_list)}

        msg = face + '昵称：' + user_nick + k + '当前总积分：' + users_score + k + '签到天数：' + days + k + '排行：' + pai_hang_dic[
            user_id]
        if qd_time == today:
            msg += k + '今日已签到'
        else:
            msg += k + '今日未签到'
        await an.send(message=msg)

    else:
        m = '[CQ:at,qq=' + user_id + ']'
        msg = Message(m) + '你还没签过到'
        await an.finish(msg)

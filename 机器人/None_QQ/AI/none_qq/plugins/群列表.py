from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event, GroupMessageEvent, Message

A = on_command('群列表', priority=5)


@A.handle()
async def S(bot: Bot, event: Event, event1: GroupMessageEvent):
    da = event.get_session_id().split('_')
    if da[0] != 'group':
        await A.send('6')
        return None
    group_id = da[1]
    data_list = await bot.call_api('get_group_member_list', **{"group_id": group_id})

    msg = ''
    face = Message('[CQ:face,id=190]')
    for i, _ in enumerate(data_list):
        msg += face + '{:>3}'.format(i + 1) + f".昵称：{_['nickname']}\u000a\t\tQQ号：{_['user_id']}\u000a"
    await A.send(msg)

from nonebot import on_command
from nonebot.adapters.onebot.v11 import Bot, Event, GroupMessageEvent

A = on_command('1', priority=5)


@A.handle()
async def S(bot: Bot, event: Event, event1: GroupMessageEvent):
    da = event.get_session_id().split('_')
    if da[0] != 'group':
        await A.send('6')
        return None
    group_id = da[1]
    data_list = await bot.call_api('get_group_member_list', **{"group_id": group_id})

    def to_json(name, uin, msg, num):
        return {"type": "node", "data": {"name": name, "uin": uin, "seq": "5123",
                                         "time": f"{1640966400+(num-1)*3600*24}", "content": msg}}

    msg = '到'
    num = 1
    messages = []
    for _ in data_list:
        messages.append(to_json(_['nickname'], _['user_id'], f'{num}\n{msg}[CQ:face,id={num}]', num))
        num += 1
    if isinstance(event, GroupMessageEvent):
        await bot.call_api(
            "send_group_forward_msg", group_id=event.group_id, messages=messages
        )

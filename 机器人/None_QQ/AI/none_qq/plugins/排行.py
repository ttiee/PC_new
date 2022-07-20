import json

from nonebot import on_keyword
from nonebot.adapters import Event
from nonebot.matcher import Matcher
from nonebot.adapters.onebot.v11 import Bot, Message
from nonebot.params import Arg, CommandArg, ArgPlainText


an = on_keyword({'积分排行', '/积分排行', '排行'}, priority=4)


data_path = r'D:\WorkSpace\PC\机器人\None_QQ\AI\data\data.json'


@an.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("ans", args)  # 如果用户发送了参数则直接赋值


@an.got('ans', prompt='请问需要多少以内的？')
async def main(event: Event, bot: Bot, ans: Message = Arg()):
    user_id = event.get_user_id()

    try:
        ans = int(str(ans))
        with open(data_path, 'r', encoding='utf-8') as f:
            users_dic = json.loads(f.read())

        sort_list = sorted(users_dic.items(), key=lambda x: x[1]['score'], reverse=True)

        pai_hang = {_[1]['nick'][-1]: (str(_[1]['score']), str(len(_[1]['days']))) for _ in sort_list[:ans]}

        face = Message('[CQ:face,id=190]')
        face1 = Message('[CQ:face,id=189]')
        k = '\u000a' + face
        k1 = '\u000a'

        msg = face1+'积分排行'+face1
        for index, _ in enumerate(pai_hang.items()):
            msg += k+'昵称：'+_[0]+k1+'\t\t'+'积分：'+_[1][0]+'\t\t'+'天数：'+_[1][1]+'\t\t'+'排行：'+str(index+1)

        await an.send(message=msg)

        user_id = event.get_user_id()
        if user_id in users_dic:
            pai_hang_dic = {_[0]: str(index + 1) for index, _ in enumerate(sort_list)}
            msg = Message(f'[CQ:at,qq={user_id}]')+k+'你的排行为：'+pai_hang_dic[user_id]
            await an.send(message=msg)
        else:
            msg = Message(f'[CQ:at,qq={user_id}]')+k1+'你还未签过到'
            await an.send(message=msg)

    except ValueError:

        msg = Message(f'[CQ:at,qq={user_id}][CQ:face,id=176]') + '请重新输入数字...'
        await an.reject(ans.template(msg))

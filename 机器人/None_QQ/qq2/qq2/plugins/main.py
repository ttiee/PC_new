from nonebot import on_command, on_keyword
from nonebot.rule import to_me
from nonebot.adapters.onebot.v11 import Message


main_ = on_keyword({"help", '帮助', '菜单', '功能', '神奇', '铁哥'}, priority=1)

main_list = ['菜单', '签到', '积分', '排行', '天气', '翻译', '名言', '/echo']
face1 = Message('[CQ:face,id=190]')
face2 = Message('[CQ:face,id=189]')
tap = '\u000a'
main_str = face1+'功能'+face1+'\u000a'+tap.join(str(index+1)+'.'+_ for index, _ in enumerate(main_list))


@main_.handle()
async def main():
    await main_.send(main_str)


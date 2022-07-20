import requests

from nonebot import on_keyword, on_command
from nonebot.adapters.onebot.v11 import Message, Bot, Event
from nonebot.matcher import Matcher
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.rule import to_me

novel = on_keyword({'下载', '小说', '文件'}, priority=10)


@novel.handle()
async def a(bot: Bot, event: Event):

    novel_path = get_novel('3')
    da = event.get_session_id().split('_')
    if da[0] != 'group':
        await novel.finish('6')
    group_id = da[1]
    msg = await bot.call_api('get_group_file_system_info', **{'group_id': group_id})
    msg1 = await bot.call_api('get_group_root_files', **{'group_id': group_id})

    await novel.send(str(msg)+'\n'+str(msg1['folders']))
    # await bot.call_api('upload_group_file', **{})


def get_novel(name: str) -> str:
    return '../novel/文件上传测试.txt'

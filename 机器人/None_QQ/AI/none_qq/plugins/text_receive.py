import os

import requests
from lxml import etree
import re
import datetime
from nonebot import on_keyword, on_command
# from nonebot.adapters import Message
from nonebot.matcher import Matcher
from nonebot.params import Arg, CommandArg, ArgPlainText, Received
from nonebot.adapters.onebot.v11 import Bot, Message, Event
from nonebot.rule import to_me

########################################
help = on_keyword({"help", "帮助"}, priority=11)


@help.handle()
async def a():
    await help.send('列表：\n1\thello\n2\t下载小说')


########################################
test = on_keyword({'1'}, priority=2)


@test.handle()
async def b(m: Event):
    com = str(m.get_message())
    if com != '1':
        print(com)
        return None
    await test.send('hello')


###################################
novel = on_keyword({'2'}, rule=to_me(), priority=2)


@novel.handle()
async def h(m: Event):
    com = str(m.get_message())
    if com != '2':
        print(com)
        return None
    await novel.send('小说|文件夹')


@novel.receive('novel')
async def c(bot: Bot, event: Event, con=Received('novel')):
    com = str(event.get_message())
    # await novel.send(con)
    # await novel.send(com)

    pattern = '^.+?\|.+?$'
    if not re.match(pattern=pattern, string=com):
        await novel.finish('请按：小说|文件夹\t的方式写')
        return None

    novel_name = com.split('|', maxsplit=1)[0]
    folder_name = com.split('|', maxsplit=1)[1]

    da = event.get_session_id().split('_')
    if da[0] != 'group':
        await novel.finish('私聊不能发文件')
    group_id = da[1]

    # 获取群文件夹数据
    msg1 = await bot.call_api('get_group_root_files', **{'group_id': group_id})
    folders = msg1['folders']

    if folders is None:
        await novel.finish('该群没有文件夹')

    folder_id = False
    for _ in folders:
        if folder_name == _['folder_name']:
            folder_id = _['folder_id'][1:]
    if not folder_id:
        await novel.finish('该文件夹不存在')

    await novel.send(f'小说：{novel_name}\n文件夹：{folder_name}')
    await upload_novel(group_id=group_id, novel_name=novel_name, folder_id=folder_id, bot=bot)


async def upload_novel(group_id: str, novel_name: str, folder_id: str, bot: Bot):
    url = 'http://www.bookshuku.com/search.html'

    xiaoshuo = {'searchkey': novel_name}
    print("xiaoshuo", xiaoshuo)
    response = requests.get(url, xiaoshuo)
    response.encoding = "utf-8"
    html = response.text
    et = etree.HTML(html)  # 网页源代码初始化，构造XPath解析对象，同时修正HTML文本
    href = et.xpath("//*[@class='searchTopic']/a/@href")[0]
    title = et.xpath("//*[@class='searchTopic']/a/@title")[0]

    if title == novel_name:
        number = re.findall(r'\d+', href)[0]  # 将书本查看界面链接的数字提取数来
        href = 'http://txt.bookshuku.com/home/down/txt/id/' + number  # 书本查看界面到书本下载界面的链接转换
        filename = r"D:/WorkSpace/PC/机器人/None_QQ/AI/none_qq/novel/" + title + ".txt"
        print("已经找到小说，正在爬取")
        f = requests.get(href)
        if len(f.content) >= 10000:
            with open(filename, "wb") as txt:
                txt.write(f.content)
            print("已经写完了")
            await novel.send("小说：" + title + "下载完成，正在上传")

            novel_path = filename
            novel_name = title + '.txt'

            await bot.call_api('upload_group_file', **{'group_id': group_id,
                                                       'file': novel_path,
                                                       'name': novel_name,
                                                       'folder': folder_id
                                                       })
            os.remove(filename)
        else:
            await novel.send('爬取到的是空页面')
    else:
        await novel.send('没有找到该小说')

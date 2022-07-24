from pyquery import PyQuery as pq
import requests
import time
import re, os

from nonebot import on_keyword, on_command
from nonebot.adapters.onebot.v11 import Message, Bot, Event
from nonebot.matcher import Matcher
from nonebot.params import Arg, CommandArg, ArgPlainText
from nonebot.rule import to_me

novel = on_keyword({'批量下载', '批量文件'}, rule=to_me(), priority=10)


@novel.handle()
async def a(bot: Bot, event: Event):
    # 获取群id
    da = event.get_session_id().split('_')
    if da[0] != 'group':
        await novel.finish('6')
    group_id = da[1]

    # 获取小说名，文件夹名
    user_command = str(event.get_message())
    if '|' not in user_command:
        await novel.finish('请按：批量文件|起始页|结束页|文件夹名 的方式写')
    try:
        start = int(user_command.split('|')[1])
        end = int(user_command.split('|')[2])
        folder_name = user_command.split('|')[3]
    except IndexError:
        await novel.finish('请按：批量文件|起始页|结束页|文件夹名 的方式写')
        return None
    except ValueError:
        await novel.finish('起始页和结束页必须是数字！')
        return None

    # await novel.send(folder_name)

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

    await novel.send('文件夹id：'+folder_id)

    await get_novel(bot=bot, start=start, end=end, folder_id=folder_id, group_id=group_id)


async def get_novel(bot: Bot, start: int, end: int, folder_id, group_id) -> None:
    _txt = get_more_href_title(page_start=start, page_end=end)
    for title, url in _txt.items():
        title = title.split(':')[0]+'.txt'
        filename = r"D:/WorkSpace/PC/机器人/None_QQ/AI/none_qq/novel/" + title
        f = requests.get(url)

        # await novel.send("开始下载小说：" + title)

        if len(f.content) >= 10000:
            with open(filename, "wb") as txt:
                txt.write(f.content)

            await novel.send("小说：" + title + "下载完成，正在上传")

            novel_path = filename
            novel_name = title

            await bot.call_api('upload_group_file', **{'group_id': group_id,
                                                       'file': novel_path,
                                                       'name': novel_name,
                                                       'folder': folder_id
                                                       })

            os.remove(filename)
        else:
            await novel.send("小说：" + title + "无价值")

    await novel.send("所有小说下载完成")


def get_a_html(number):
    url = 'http://www.bookshuku.com/xuanhuan/index_{}.html'.format(number)
    response = requests.get(url)
    response.encoding = "utf-8"
    html = response.text
    return html


def get_a_href_title(html):
    doc = pq(html)  # 获取网页源码的节点
    a = doc('.mainSoftName a')  # 找到mainListName后面的a节点

    txt_title = []  # 保存书名的列表
    txt_url = []  # 保存书本的链接

    for item in a.items():
        href1 = item.attr('href')  # 获取节点属性---书本查看界面
        # http://www.bookshuku.com/bookinfo/77994.html
        # http://txt.bookshuku.com/home/down/txt/id/77994
        list = re.findall(r'\d+', href1)  # 将书本查看界面链接的数字提取数来
        number = list[0]
        href = 'http://txt.bookshuku.com/home/down/txt/id/' + number  # 书本查看界面到书本下载界面的链接转换

        title = item.text()  # 获取节点文本---书名

        txt_url.append(href)
        txt_title.append(title)

    txt = dict(zip(txt_title, txt_url))  # 将书名和链接组成字典
    return txt


def get_more_href_title(page_start: int, page_end: int):
    txt = dict()

    for i in range(page_start, page_end + 1):
        html = get_a_html(i)
        txt1 = get_a_href_title(html)

        txt.update(txt1)  # 将字典txt1添加到字典txt中

    return txt

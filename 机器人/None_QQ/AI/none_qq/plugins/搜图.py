import json
import requests
import random

from nonebot.rule import to_me
from nonebot import on_command, on_keyword
from nonebot.adapters.onebot.v11 import MessageSegment, Bot, Event

from nonebot.matcher import Matcher
from nonebot.adapters import Message
from nonebot.params import Arg, CommandArg, ArgPlainText

ND = on_command("网图",aliases={"搜图"}, priority=2,block=True)
@ND.handle()
async def handle_first_receive(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("Name", args)  # 如果用户发送了参数则直接赋值


@ND.got("Name", prompt="你想找哪个人物呀？小可爱~")
async def handle_city(Name: Message = Arg(), sname: str = ArgPlainText("Name")):
    try:
        print("-----网图测试")
        print(sname)
        print("-----网图测试")
        url = f'https://api.iyk0.com/swt/?msg={sname}'
        url = str(requests.get(url).text)
        await ND.send(MessageSegment.image(url))
    except Exception as e:
        await ND.send("搜图插件出现故障，请联系神奇")


st = on_keyword(keywords={'每日一图'}, priority=2,block=True)
@st.handle()
async def st_(bot: Bot, event: Event):
    try:
        url=str(get_setu())
        if int(event.get_user_id()) != event.self_id:
            await st.send(MessageSegment.image(file=str(url)))
    except Exception as e:
        await st.send("每日一图插件出现故障，请联系神奇")


# 获取图片
def get_setu():
    url='https://api.iyk0.com/ecy/api.php'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36'
    }
    res = requests.get(url,headers=headers)
    c = res.url
    return c


def get_biao(text:str):
    url = ('https://api.iyk0.com/sbqb/?msg='+text)
    r = requests.get(url)
    result = json.loads(r.content)
    l = result['sum']
    k = random.randint(0, l)
    message = result['data_img'][k]['img']
    print(message)
    return message

BQB = on_command("表情包", rule=to_me(),priority=2,block=True)

@BQB.handle()
async def BQB_(matcher: Matcher, args: Message = CommandArg()):
        plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
        if plain_text:
            matcher.set_arg("biao", args)  # 如果用户发送了参数则直接赋值



@BQB.got("biao", prompt="你想查询神马表情包(@_@)...")
async def handle_biao(biao: Message = Arg(), biao_name: str = ArgPlainText("biao")):
    print(biao_name)
    biaoqingbao = get_biao(biao_name)
    await BQB.send(MessageSegment.image(biaoqingbao))

def get_wangzhe(text:str):
    url = ('https://api.iyk0.com/wzcz/?msg='+text)
    r = requests.get(url)
    result = json.loads(r.content)
    message = result['img']
    print(message)
    return message

# 王者荣耀出装
WZRY = on_command("王者荣耀", priority=2,block=True)
@WZRY.handle()
async def WZ_(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("king", args)  # 如果用户发送了参数则直接赋值


@WZRY.got("king", prompt="你想查询什么英雄(@_@)...")
async def handle_WZ(king: Message = Arg(), king_name: str = ArgPlainText("king")):
    try:
        wangzhe = get_wangzhe(king_name)
        await WZRY.send(MessageSegment.image(wangzhe))
    except Exception as e:
        await WZRY.send("查询失败")
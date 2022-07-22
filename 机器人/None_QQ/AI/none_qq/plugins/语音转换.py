import requests
from nonebot import on_command
from nonebot.adapters import Message
from nonebot.adapters.onebot.v11 import MessageSegment
from nonebot.matcher import Matcher
from nonebot.params import Arg, CommandArg, ArgPlainText


# 语音转换
def get_yuying(text:str):
    url = ('https://api.iyk0.com/yy/?msg='+text)
    r = requests.get(url)
    message = r.text
    print(message)
    return message


YYZH = on_command("语音转换", priority=2,block=True)
@YYZH.handle()
async def YY_(matcher: Matcher, args: Message = CommandArg()):
    plain_text = args.extract_plain_text()  # 首次发送命令时跟随的参数，例：/天气 上海，则args为上海
    if plain_text:
        matcher.set_arg("yuying", args)  # 如果用户发送了参数则直接赋值


@YYZH.got("yuying", prompt="你想转换什么")
async def handle_YY(yuying: Message = Arg(), yuying_name: str = ArgPlainText("yuying")):
    try:
        huan = str(get_yuying(yuying_name))
        huan = huan.replace('\n', '')
        print("转换内容: ",huan)
        await YYZH.send(MessageSegment.record(huan))
    except Exception as e:
        await YYZH.send("转换失败")
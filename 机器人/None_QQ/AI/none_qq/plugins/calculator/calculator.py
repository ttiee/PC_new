from nonebot import on_command
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from math import sqrt, factorial, log
import re
import os
from nonebot.adapters.cqhttp import MessageSegment
import time
from .config import Config

__plugin_name__ = 'calculator'
__plugin_usage__ = '用法：计算器。'

dir_path = 'file:///' + os.path.split(os.path.realpath(__file__))[0] + '/img/'

# 这是一张图片，会在击杀复读者时发送
think_img = dir_path + 'think.gif'

# 记录上一次响应时间， 初始化为开机时间-cd时间
last_response = time.time() - Config.cd

calculator_help = on_command("计算帮助", priority=Config.priority)
@calculator_help.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    await calculator_help.finish(f'''关于计算模块的使用说明：
使用命令为"/计算 [算式]"
命令响应冷却时间为：{Config.cd}秒
警告：由于遭到大数据滥用，现已不支持幂运算！
警告：阶乘计算输入值不得超过{Config.factorial_limit}！

目前支持的输入内容包括(由张3作为示例)：
空格与换行符:不会影响计算
3:整数
3.3:小数
3+3j:虚数
3e3或3e-3或3E3:科学计数法表示的数字
():小括号
+-*/:四则运算或负号
abs(-3):绝对值
sqrt(3):平方根
//:整除
%:求余数
factorial(3):阶乘
log(3,3):对数''')

calculator = on_command("计算", priority=Config.priority)
@calculator.handle()
async def handle_first_receive(bot: Bot, event: Event, state: T_State):
    global last_response
    use_calculator = False
    ids = event.get_session_id()
    # 如果这是一条群聊信息
    if ids.startswith("group"):
        _, group_id, user_id = event.get_session_id().split("_")
        if group_id in Config.used_in_group:
            use_calculator = True
    else:
        user_id = ids
        use_calculator = True
    if use_calculator:
        # 检测响应cd， 如果允许则继续，管理员无视冷却cd
        if time.time() - last_response >= Config.cd or user_id in Config.super_uid:
            # 将中文的括号与逗号都替换为英文的
            msg = str(event.get_message()).strip().replace(' ', '').replace('\r\n','').replace('\n','').replace('（','(').replace('）',')').replace('，',',').replace('/计算', '')
            require = "(\d| |\+|\-|\*|/|\(|\)|abs\(|sqrt\(|factorial\(|%|E|e|\.|log\(|\,|j)*"
            # 判断是否有过大阶乘输入
            facts = re.findall("factorial\(\d*\)", msg)
            facts = list(map(lambda x: int(x[10:-1]), facts))
            large_fact = False
            for fact in facts:
                if fact > Config.factorial_limit:
                    large_fact = True
                    break
            # 未通过正则匹配
            if msg != re.match(require, msg, flags=0).group() or "**" in msg:
                last_response = time.time()
                await calculator.finish("错误：输入算式中含有非法格式，请使用/计算帮助查询规范。"+MessageSegment.image(think_img))
            # 如果阶乘输入过大
            elif large_fact:
                await calculator.finish("错误：输入算式中阶乘输入值过大，请使用/计算帮助查询规范。" + MessageSegment.image(think_img))
            # 通过匹配
            else:
                try:
                    # 将字符串作为代码运行计算，并保留5位小数防止浮点数的尾数溢出
                    result = round(eval(msg), 5)
                except ZeroDivisionError:
                    last_response = time.time()
                    await calculator.finish("错误：除数为零。" + MessageSegment.image(think_img))
                except:
                    last_response = time.time()
                    await calculator.finish("错误：输入算式并不是正确的算式。"+MessageSegment.image(think_img))
                else:
                    last_response = time.time()
                    await calculator.finish("计算结果：" + str(result) + MessageSegment.image(think_img))


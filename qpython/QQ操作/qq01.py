import random

import re
from qqbot import QQBotSlot as qqbotslot, RunBot

from d import dictList


@qqbotslot
def onQQMessage(bot, contact, member, content):
    res_url = '[^.*?[]]'
    link = re.findall(res_url, str(content), re.I | re.S | re.M)
    res_url2 = '/Emoji.*?'
    link2 = re.findall(res_url2, str(content), re.I | re.S | re.M)
    print('*****',link)
    if 'hello' in str(content):
        bot.SendTo(contact, str(random.choice(dictList["niHao"])))
    elif '在' in str(content):
        bot.SendTo(contact, str(random.choice(dictList["zai"])))
    elif '你好' in str(content):
        bot.SendTo(contact, str(random.choice(dictList["niHao"])))
    elif '啊' in str(content):
        bot.SendTo(contact,  str(random.choice(dictList["a"])))
    elif '嗯' in str(content):
        bot.SendTo(contact,  str(random.choice(dictList["en"])))
    elif '哦' in str(content):
        bot.SendTo(contact, str(random.choice(dictList["everyThing"])))
    elif '没事' in str(content):
        bot.SendTo(contact,  str(random.choice(dictList["everyThing"])))
    elif '/表情' in str(content):
        bot.SendTo(contact,  str(random.choice(dictList["everyThing"])))
    elif '/白眼' in str(content):
        bot.SendTo(contact,  str(random.choice(dictList["baiYan"])))
    elif '什么' in str(content):
        bot.SendTo(contact,  str(random.choice(dictList["shenMe"])))
    elif '确' in str(content):
        bot.SendTo(contact,  str(random.choice(dictList["everyThing"])))
    elif '拜拜' in str(content):
        bot.SendTo(contact, '你确定要和我说再见了吗？')
    elif len(link):
        bot.SendTo(contact, str(random.choice(dictList["everyThing"])))
    elif '/偷笑' in str(content):
        bot.SendTo(contact, str(random.choice(dictList["everyThing"])))
    elif '..' in str(content):
        bot.SendTo(contact, str(random.choice(dictList["everyThing"])))
    elif '。。。' in str(content):
        bot.SendTo(contact, str(random.choice(dictList["everyThing"])))
    elif len(link2):
        bot.SendTo(contact, str(random.choice(dictList["everyThing"])))
    elif '哈' in str(content):
        bot.SendTo(contact, str(random.choice(dictList["everyThing"])))
    #特殊标记字符，停止监听
    elif '++' in content:
        bot.SendTo(contact, '晚安，好梦')
        bot.Stop()


if __name__ == '__main__':
    RunBot()

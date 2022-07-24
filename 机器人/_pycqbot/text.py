from pycqBot.cqApi import cqHttpApi
from pycqBot import Message

b1 = cqHttpApi(host='http://127.0.0.1:5701/')


# echo 函数
def echo(command_data, message: Message):
    # 回复消息
    message.reply(" ".join(command_data))


bot = b1.create_bot(
    group_id_list=[
        # 需处理的 QQ 群信息 为空处理所有
        "566077032",
        '762093001'
    ],
)

# 设置指令为 echo
bot.command(echo, "echo", {
    # echo 帮助
    "help": [
        "#echo - 输出文本"
    ]
})

bot.start(go_cqhttp_path=r'D:/QQ机器人/go-cqhttp_windows_amd64')

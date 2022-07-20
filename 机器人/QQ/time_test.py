import time
import re
import send_msg
import random


msgs = [
    '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" templateID="1" action="web" brief="" sourceMsgId="0" url="https://qm.qq.com/cgi-bin/qm/qr?k=wyw10nH14NxBzBmM2DZK_bj9y9yX-IJL" flag="0" adverSign="0" multiMsgFlag="0"><item layout="2"><audio cover="https://python3student.github.io/img/avatar.jpg" src="http://music.163.com/song/media/outer/url?id=31365604" /><title>你从未离去</title><summary>『作者』神奇</summary></item><source name="神奇永远的神！" icon="https://python3student.github.io/img/avatar.jpg" url="https://python3student.github.io/img/avatar.jpg" action="app" a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" /></msg>,resid=60]',
    '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" templateID="1" action="web" brief="" sourceMsgId="0" url="https://qm.qq.com/cgi-bin/qm/qr?k=wyw10nH14NxBzBmM2DZK_bj9y9yX-IJL" flag="0" adverSign="0" multiMsgFlag="0"><item layout="2"><audio cover="https://python3student.github.io/img/avatar.jpg" src="https://music.163.com/song/media/outer/url?id=449818326.mp3" /><title>鹿 be free</title><summary>『作者』神奇</summary></item><source name="神奇永远的神！" icon="https://python3student.github.io/img/avatar.jpg" url="https://python3student.github.io/img/avatar.jpg" action="app" a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" /></msg>,resid=60]',
    '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" templateID="1" action="web" brief="" sourceMsgId="0" url="https://qm.qq.com/cgi-bin/qm/qr?k=wyw10nH14NxBzBmM2DZK_bj9y9yX-IJL" flag="0" adverSign="0" multiMsgFlag="0"><item layout="2"><audio cover="https://python3student.github.io/img/avatar.jpg" src="https://music.163.com/song/media/outer/url?id=548252595.mp3" /><title>勇往直前</title><summary>『作者』神奇</summary></item><source name="神奇永远的神！" icon="https://python3student.github.io/img/avatar.jpg" url="https://python3student.github.io/img/avatar.jpg" action="app" a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" /></msg>,resid=60]',
    '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" templateID="1" action="web" brief="" sourceMsgId="0" url="https://qm.qq.com/cgi-bin/qm/qr?k=wyw10nH14NxBzBmM2DZK_bj9y9yX-IJL" flag="0" adverSign="0" multiMsgFlag="0"><item layout="2"><audio cover="https://python3student.github.io/img/avatar.jpg" src="https://music.163.com/song/media/outer/url?id=28613172.mp3" /><title>伴你成长</title><summary>『作者』神奇</summary></item><source name="神奇永远的神！" icon="https://python3student.github.io/img/avatar.jpg" url="https://python3student.github.io/img/avatar.jpg" action="app" a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" /></msg>,resid=60]',
    '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" templateID="1" action="web" brief="" sourceMsgId="0" url="https://qm.qq.com/cgi-bin/qm/qr?k=wyw10nH14NxBzBmM2DZK_bj9y9yX-IJL" flag="0" adverSign="0" multiMsgFlag="0"><item layout="2"><audio cover="https://python3student.github.io/img/avatar.jpg" src="https://music.163.com/song/media/outer/url?id=27896762.mp3" /><title>终会与你同行</title><summary>『作者』神奇</summary></item><source name="神奇永远的神！" icon="https://python3student.github.io/img/avatar.jpg" url="https://python3student.github.io/img/avatar.jpg" action="app" a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" /></msg>,resid=60]',
    '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" templateID="1" action="web" brief="" sourceMsgId="0" url="https://qm.qq.com/cgi-bin/qm/qr?k=wyw10nH14NxBzBmM2DZK_bj9y9yX-IJL" flag="0" adverSign="0" multiMsgFlag="0"><item layout="2"><audio cover="https://python3student.github.io/img/avatar.jpg" src="https://music.163.com/song/media/outer/url?id=1873321491.mp3" /><title>Wake</title><summary>『作者』神奇</summary></item><source name="神奇永远的神！" icon="https://python3student.github.io/img/avatar.jpg" url="https://python3student.github.io/img/avatar.jpg" action="app" a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" /></msg>,resid=60]',
    '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" templateID="1" action="web" brief="" sourceMsgId="0" url="https://qm.qq.com/cgi-bin/qm/qr?k=wyw10nH14NxBzBmM2DZK_bj9y9yX-IJL" flag="0" adverSign="0" multiMsgFlag="0"><item layout="2"><audio cover="https://python3student.github.io/img/avatar.jpg" src="https://music.163.com/song/media/outer/url?id=36990266.mp3" /><title>Faded</title><summary>『作者』神奇</summary></item><source name="神奇永远的神！" icon="https://python3student.github.io/img/avatar.jpg" url="https://python3student.github.io/img/avatar.jpg" action="app" a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" /></msg>,resid=60]'
]

b = 0
while 1:
    t = time.ctime()

    fen = int(re.findall('\d*:(\d*):\d', t)[0])
    miao = int(re.findall('\d*:\d*:(\d)', t)[0])

    if fen == 0 and b == 0:
        send_msg.send_msg({'msg_type': 'group', 'number': 1143107466, 'msg': '整点报时'})
        send_msg.send_msg({'msg_type': 'group', 'number': 1143107466, 'msg': msgs[random.randint(0, len(msgs) - 1)]})
        send_msg.send_msg({'msg_type': 'group', 'number': 1143107466, 'msg': '时间：'+time.ctime()})
        print('报时成功')
        b = 1

    if fen == 1 and b == 1:
        print('回调成功')
        b = 0
        print('休眠3480秒中......')
        time.sleep(3480)
        print('休眠完成')

    if fen == 20:
        print('休眠2280秒中......')
        time.sleep(2280)
        print('休眠完成')

    if fen == 40:
        print('休眠1080秒中......')
        time.sleep(1080)
        print('休眠完成')
    if miao == 3:
        print('休眠54秒中......')
        time.sleep(54)
        print('休眠完成')

import re

from send_msg import send_msg
from receive import rev_msg
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
msg_str = '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" templateID="1" ' \
          'action="web" brief="" sourceMsgId="0" url="https://qm.qq.com/cgi-bin/qm/qr?k=wyw10nH14NxBzBmM2DZK_bj9y9yX-IJL" flag="0" adverSign="0" ' \
          'multiMsgFlag="0"><item layout="2"><audio cover="https://python3student.github.io/img/avatar.jpg" ' \
          'src="https://music.163.com/song/media/outer/url?id={0}.mp3" ' \
          '/><title>{2}</title><summary>『作者』{1}</summary></item><source name="神奇永远的神！" ' \
          'icon="https://python3student.github.io/img/avatar.jpg" ' \
          'url="https://python3student.github.io/img/avatar.jpg" action="app" a_actionData="com.netease.cloudmusic" ' \
          'i_actionData="tencent100495085://" appid="100495085" /></msg>,resid=60] '


def main():
    while True:
        rev = rev_msg()
        print(rev)

        if rev is None:
            continue
        if rev["post_type"] == "message":
            # print(rev) #需要功能自己DIY
            if rev["message_type"] == "private":  # 私聊
                qq = rev['sender']['user_id']
                if qq == 2845404905 or qq == 3439453420:
                    pass
                elif qq == 1679194340 or qq == 1679194340:
                    import music2
                    sonng_msg = music2.music_search(rev['raw_message'])
                    send_msg({'msg_type': 'group', 'number': qq, 'msg': sonng_msg})
                elif '在吗' in rev['raw_message']:
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': '在呢'})
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': '[CQ:face,id=317,type=sticker]'})
                elif '随机音乐' in rev['raw_message']:
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': msgs[random.randint(0, len(msgs) - 1)]})
                elif '点歌' in rev['raw_message']:
                    import music2
                    kee = re.sub('点歌', '', rev['raw_message'])
                    song_list = music2.music_search(kee)
                    sonng_msg, song_url = song_list[0], song_list[1]
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': sonng_msg})
                    send_msg({'msg_type': 'private', 'number': qq, 'msg': '音乐名：{1}\u000a作者：{2}\u000a音乐链接：{0}'.format(song_url, song_list[2], song_list[3])})
                else:
                    # send_msg({'msg_type': 'private', 'number': qq, 'msg': msgs[random.randint(0, len(msgs) - 1)]})
                    send_msg({'msg_type': 'private', 'number': qq,
                              'msg': '[CQ:face,id=190]可以点歌或随机音乐[CQ:face,id=190]\u000a[CQ:face,id=190]格式：点歌xxx[CQ:face,id=190]\u000a[CQ:face,id=190]格式：随机音乐[CQ:face,id=190]'})

                    send_msg({'msg_type': 'private', 'number': qq, 'msg': '[CQ:poke,qq={}]'.format(qq)})
                    # send_msg({'msg_type': 'private', 'number': qq, 'msg': '在呢,{}\t可以\n1.随机音乐\n'})
            elif rev["message_type"] == "group":  # 群聊
                group = rev['group_id']
                if '时间' in rev["raw_message"]:
                    import datetime
                    nn = datetime.datetime.now().strftime("%Y-%m-%d (%A) %H:%M:%S")
                    send_msg({'msg_type': 'group', 'number': group, 'msg': nn})

                # if group == 762093001 or group == 762093001:
                #     import music2
                #     sonng_msg = music2.music_search(rev['raw_message'])
                #     send_msg({'msg_type': 'group', 'number': group, 'msg': sonng_msg})
                if "[CQ:at,qq=469784630]" in rev["raw_message"]:
                    if rev['raw_message'].split(' ')[1] == '在吗':
                        qq = rev['sender']['user_id']
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:poke,qq={}]'.format(qq)})
                        send_msg({'msg_type': 'group', 'number': group, 'msg': msgs[random.randint(0, len(msgs) - 1)]})
                        # send_msg({'msg_type': 'group', 'number': group, 'msg': '在呢,{}\t可以\n1.@我+随机音乐\n2.@我+播放+歌名'})
                    elif '点歌' in rev['raw_message']:
                        import music2
                        kee = re.sub('(\[CQ:at,qq=469784630\])|(点歌)','', rev['raw_message'])
                        song_list = music2.music_search(kee)
                        sonng_msg, song_url = song_list[0], song_list[1]
                        send_msg({'msg_type': 'group', 'number': group, 'msg': sonng_msg})
                        if song_url is not None:
                            send_msg({'msg_type': 'group', 'number': group, 'msg': '音乐名：{1}\u000a作者：{2}\u000a音乐链接：{0}'.format(song_url, song_list[2], song_list[3])})
                        # send_msg({'msg_type': 'group', 'number': group, 'msg': msgs[random.randint(0, len(msgs) - 1)]})
                    elif '随机音乐' in rev['raw_message']:
                        send_msg({'msg_type': 'group', 'number': group, 'msg': msgs[random.randint(0, len(msgs) - 1)]})
                    # elif '播放' in rev['raw_message']:
                    #     ming = rev['raw_message'][len('[CQ:at,qq=469784630]播放)]')-1:]
                    #     print(ming)
                    #     id = get_id(ming)
                    #     send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:music,type=163,id={}]'.format(id)})
                    else:
                        qq = rev['sender']['user_id']
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:poke,qq={}]'.format(qq)})
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:face,id=189]'})
                        send_msg({'msg_type': 'group', 'number': group, 'msg': '[CQ:face,id=190]可以@我加点歌或@我加随机音乐[CQ:face,id=190]\u000a[CQ:face,id=190]格式：@我点歌xxx[CQ:face,id=190]\u000a[CQ:face,id=190]格式：@我随机音乐[CQ:face,id=190]'})
                        # send_msg({'msg_type': 'group', 'number': group, 'msg': '在在在！\n1.@我+随机音乐\n2.@我+播放+歌名'})
            else:
                continue
        elif rev['post_type'] == "notice":  # 回戳
            if rev['sub_type'] == 'poke':
                if rev['target_id'] == 469784630:
                    if 'group_id' in rev:
                        send_msg({'msg_type': 'group', 'number': rev['group_id'],
                                  'msg': '[CQ:poke,qq={}]'.format(rev['sender_id'])})
                    else:
                        send_msg({'msg_type': 'private', 'number': rev['sender_id'],
                                  'msg': '[CQ:poke,qq={}]'.format(rev['sender_id'])})
                    # if rev['target_id'] == '469784630' and rev['sub_type'] == 'poke':
                    #     send_msg({'msg_type': 'private', 'number': rev['sender_id'], 'msg': '[CQ:poke,qq={}]'.format(rev['sender_id'])})
                    # if rev['target_id'] == 469784630 and rev['sub_type'] == 'poke' :
                    #     send_msg({'msg_type': 'group', 'number': rev['group_id'], 'msg': '[CQ:poke,qq={}]'.format(rev['sender_id'])})
        else:  # rev["post_type"]=="meta_event":
            continue


def a():
    try:
        main()
    except:
        print('\n\n\n' + '#' * 100 + '\n\n\n')
        return a()


if __name__ == '__main__':
    a()

# -*- coding: UTF-8 -*-
import time

from send_msg import send_msg
from get_group import get_group

resp_dict1 = {'msg_type': 'private', 'number': 2207082899,
              'msg': '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" '
                     'templateID="1" action="web" brief="" sourceMsgId="0" url="https://qm.qq.com/cgi-bin/qm/qr?k=HpooctxyP4208KfcB7tU7YfQw_Xc4D1q" '
                     'flag="0" adverSign="0" multiMsgFlag="0"><item layout="2"><audio '
                     'cover="https://qlogo4.store.qq.com/qzone/2207082899/2207082899/100?1651840987" '
                     'src="http://music.163.com/song/media/outer/url?id=1901371647" '
                     '/><title>孤勇者</title><summary>『作者』胡岩</summary></item><source name="胡岩永远的神！" '
                     'icon="https://qlogo4.store.qq.com/qzone/2207082899/2207082899/100?1651840987" '
                     'url="https://qlogo4.store.qq.com/qzone/2207082899/2207082899/100?1651840987" action="app" '
                     'a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" '
                     '/></msg>,resid=60]'}

resp_dict = {'msg_type': 'group', 'number': 1143107466, 'msg': '[CQ:at,qq=1692851288]'}
resp_dict2 = {'msg_type': 'group', 'number': 1143107466,
              'msg': '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" '
                     'templateID="1" action="web" brief="" sourceMsgId="0" url="https://python3student.github.io/" '
                     'flag="0" adverSign="0" multiMsgFlag="0"><item layout="2"><audio '
                     'cover="https://qlogo3.store.qq.com/qzone/469784630/469784630/100?1644649703" '
                     'src="http://music.163.com/song/media/outer/url?id=31365604" '
                     '/><title>你从未离去</title><summary>『作者』神奇</summary></item><source name="神奇永远的神！" '
                     'icon="https://qlogo3.store.qq.com/qzone/469784630/469784630/100?1644649703" '
                     'url="https://qlogo3.store.qq.com/qzone/469784630/469784630/100?1644649703ttps://python3student.github.io/img/avatar.jpg" action="app" '
                     'a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" '
                     '/></msg>,resid=60]'}
resp_dict3 = {'msg_type': 'private', 'number': 1679194340, 'msg': '[CQ:tts,text=谢军敏这是一条测试消息]'}
resp_dict4 = {'msg_type': 'group', 'number': 1143107466, 'msg': '[CQ:tts,text=谢军敏这是一条测试消息]'}
liwu = {'msg_type': 'group', 'number': 1143107466, 'msg': '[CQ:gift,qq=1642883508,id=2]'}
card = {'msg_type': 'private', 'number': 1679194340,
        'msg': '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" templateID="1" action="web" brief="&#91;分享&#93; 十年" sourceMsgId="0" url="https://i.y.qq.com/v8/playsong.html?_wv=1&amp;songid=4830342&amp;souce=qqshare&amp;source=qqshare&amp;ADTAG=qqshare" flag="0" adverSign="0" multiMsgFlag="0" ><item layout="2"><audio cover="http://imgcache.qq.com/music/photo/album_500/26/500_albumpic_89526_0.jpg" src="http://ws.stream.qqmusic.qq.com/C400003mAan70zUy5O.m4a?guid=1535153710&amp;vkey=D5315B8C0603653592AD4879A8A3742177F59D582A7A86546E24DD7F282C3ACF81526C76E293E57EA1E42CF19881C561275D919233333ADE&amp;uin=&amp;fromtag=3" /><title>十年</title><summary>陈奕迅</summary></item><source name="QQ音乐" icon="https://i.gtimg.cn/open/app_icon/01/07/98/56/1101079856_100_m.png" url="http://web.p.qq.com/qqmpmobile/aio/app.html?id=1101079856" action="app"  a_actionData="com.tencent.qqmusic" i_actionData="tencent1101079856://" appid="1101079856" /></msg>]'}
music = {'msg_type': 'private', 'number': 1679194340, 'msg': '[CQ:music,type=163,id=28949129]'}
j = {'msg_type': 'private', 'number': 1679194340,
     'msg': '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<msg serviceID="1">'
            '<item layout="4">'
            '<title>神奇666</title>'
            '<picture cover="https://python3student.github.io/img/top.jpg"/>'
            '</item>'
            '</msg>]'}
q = {'msg_type': 'private', 'number': 1679194340,
     'msg': '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<msg serviceID="1">'
            '<item><title>生死8秒！女司机高速急刹, 他一个操作救下一车性命</title></item>'
            '<source name="官方认证消息" icon="https://python3student.github.io/img/top.jpg" action="" appid="-1" />'
            '</msg>'}
ban = {'msg_type': 'group', 'number': 1143107466,
       'msg': '[CQ:record,file=https://music.163.com/song/media/outer/url?id=28613172.mp3]'}
face = {'msg_type': 'private', 'number': 3225685814, 'msg': '[CQ:face,id={}]'}

json_msg = '[CQ:json,data={"app":"com.tencent.miniapp_01"&#44;"config":{"autoSize":0&#44;"ctime":1652082785&#44;"forward":1&#44;"height":0&#44;"token":"b4c065b52082a74bea5f8a77e72db43b"&#44;"type":"normal"&#44;"width":0}&#44;"desc":"哔哩哔哩"&#44;"extra":{"app_type":1&#44;"appid":100951776&#44;"uin":1642883508}&#44;"meta":{"detail_1":{"appType":0&#44;"appid":"1109937557"&#44;"desc":"手冲 VS 器冲"&#44;"gamePoints":""&#44;"gamePointsUrl":""&#44;"host":{"nick":"pToTq"&#44;"uin":1642883508}&#44;"icon":"http://miniapp.gtimg.cn/public/appicon/432b76be3a548fc128acaa6c1ec90131_200.jpg"&#44;"preview":"pubminishare-30161.picsz.qpic.cn/c332dbdc-0b82-4243-86fe-1c7fb046dee7"&#44;"qqdocurl":"https://qm.qq.com/cgi-bin/qm/qr?k=HpooctxyP4208KfcB7tU7YfQw_Xc4D1q"&#44;"scene":1036&#44;"shareTemplateData":{}&#44;"shareTemplateId":"8C8E89B49BE609866298ADDFF2DBABA4"&#44;"showLittleTail":""&#44;"title":"哔哩哔哩"&#44;"url":"m.q.qq.com/a/s/ea0700e588015fc8b87633156c4ba9fb"}}&#44;"needShareCallBack":false&#44;"prompt":"&#91;QQ小程序&#93;哔哩哔哩"&#44;"ver":"1.0.0.19"&#44;"view":"view_8C8E89B49BE609866298ADDFF2DBABA4"}]'

xml_msg1 = '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8"?><ui version="4.0"><class>MainWindow</class><widget class="QMainWindow" name="MainWindow"><property name="geometry"><rect><x>0</x><y>0</y><width>800</width><height>600</height></rect></property><property name="windowTitle"><string>MainWindow</string></property><widget class="QWidget" name="centralwidget"><widget class="QPushButton" name="pushButton"><property name="geometry"><rect><x>-10</x><y>0</y><width>291</width><height>151</height></rect></property><property name="text"><string>PushButton</string></property></widget></widget><widget class="QMenuBar" name="menubar"><property name="geometry"><rect><x>0</x><y>0</y><width>800</width><height>26</height></rect></property></widget><widget class="QStatusBar" name="statusbar"/></widget><resources/><connections/></ui>]'
xml_msg2 = '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>actionData="AppCmd://OpenContactInfo/?uin=85443298"a_actionData="mqqapi://card/show_pslcard?src_type=internal&source=sharecard&version=1&uin=85443298"i_actionData="mqqapi://card/show_pslcard?src_type=internal&source=sharecard&version=1&uin=85443298"brief="[QQ红包]恭喜发财" flag="2" url="https://qm.qq.com/cgi-bin/qm/qr?k=HpooctxyP4208KfcB7tU7YfQw_Xc4D1q">]'
json_msg1 = '[CQ:json,data={"app":"com.tencent.structmsg","desc":"新闻","view":"news","ver":"0.0.0.1","prompt":"[分享]好友邀请你玩永劫无间！","appID":"","sourceName":"","actionData":"","actionData_A":"","sourceUrl":"","meta":{"news":{"action":"","android_pkg_name":"","app_type":1,"appid":1104466820,"desc":"运用丰富的武器战胜敌人，世界的真相将向胜者展开","jumpUrl":"https://liflag.cn?_wv=2147484679&_wwv=4&ADTAG=ark.hdshare&pf=invite&appid=1104466820&notShowPub=0&asyncMode=3&appType=1&_nav_bgclr=ffffff&_nav_titleclr=ffffff&_nav_txtclr=ffffff&_nav_anim=true&_nav_alpha=0&invite_uin=251580158&invite_openid=D554C3DD415FA2EB6B78D0ECA6964092&recv_uin=229670104","preview":"https://wx4.sinaimg.cn/mw690/0062WSWoly1gs9kqwl8f0j322o22okjn.jpg","source_icon":"","source_url":"","tag":"永劫无间","title":"好友邀请你上线了！"}}}]'
json_msg2 = '[CQ:json,data={"app":"com.tencent.miniapp","desc":"","view":"all","ver":"1.0.0.89","prompt":"来报时啦","appID":"","sourceName":"","actionData":"","actionData_A":"","sourceUrl":"","meta":{"all":{"buttons":[{"action":"http://www.qq.com","name":"2021年5月25日  12:20:00"}],"jumpUrl":"","preview":"http://gchat.qpic.cn/gchatpic_new/543486646/543486646-0-17A70505061636CEE684DF3842C7B6A8/0?term=2&kp=1&pt=0&bo=4AEOAQAAAAACd70!&tl=1&vuin=2292380798&tm=1597590000&t=5#sce=14-1-1&rf=v1_ht5_qz_3.4.0_001_idc_b-4-0","summary":"\n----------整点报时----------\n每日一言：待至暮年归,挽手戏落日.","title":"整点报时"}},"config":{"forward":true},"text":"","extraApps":[],"sourceAd":"","extra":""}'
cardimage_msg1 = '[CQ:cardimage,file=http://gchat.qpic.cn/gchatpic_new/543486646/543486646-0-17A70505061636CEE684DF3842C7B6A8/0?term=2&kp=1&pt=0&bo=4AEOAQAAAAACd70!&tl=1&vuin=2292380798&tm=1597590000&t=5#sce=14-1-1&rf=v1_ht5_qz_3.4.0_001_idc_b-4-0]'
# http://gchat.qpic.cn/gchatpic_new/543486646/543486646-0-17A70505061636CEE684DF3842C7B6A8/0?term=2&kp=1&pt=0&bo=4AEOAQAAAAACd70!&tl=1&vuin=2292380798&tm=1597590000&t=5#sce=14-1-1&rf=v1_ht5_qz_3.4.0_001_idc_b-4-0
img_msg_msg = '[CQ:video,file=http://gchat.qpic.cn/gchatpic_new/543486646/543486646-0-17A70505061636CEE684DF3842C7B6A8/0?term=2&kp=1&pt=0&bo=4AEOAQAAAAACd70!&tl=1&vuin=2292380798&tm=1597590000&t=5#sce=14-1-1&rf=v1_ht5_qz_3.4.0_001_idc_b-4-0]'
share_msg = '[CQ:share,url=http://baidu.com,title=百度,image=http://gchat.qpic.cn/gchatpic_new/543486646/543486646-0-17A70505061636CEE684DF3842C7B6A8/0?term=2&kp=1&pt=0&bo=4AEOAQAAAAACd70!&tl=1&vuin=2292380798&tm=1597590000&t=5#sce=14-1-1&rf=v1_ht5_qz_3.4.0_001_idc_b-4-0]'
xml_msg3 = '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="1" templateID="1234" action="web" brief="清屏!" sourceMsgId="2" url="" flag="2" adverSign="0" multiMsgFlag="0"><item layout="5" advertiser_id="0" aid="0"><picture cover="http://gchat.qpic.cn/gchatpic_new/0/0-0-FE78A07C337C18CA8744113A86A62AAF/0?term=2" w="0" h="0" /><title></title><summary></summary></item><item layout="6" advertiser_id="0" aid="0"><summary size="300" color="#EAFA04">神奇清屏专用</summary><hr hidden="false" style="15" /></item><source name="" icon="" action="" appid="-1" /></msg>]'
xml_msg4 = '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="1" templateID="1234" action="web" brief="清屏!" sourceMsgId="2" url="" flag="2" adverSign="0" multiMsgFlag="0"><item layout="5" advertiser_id="0" aid="0"><picture cover="# http://gchat.qpic.cn/gchatpic_new/543486646/543486646-0-17A70505061636CEE684DF3842C7B6A8/0?term=2&kp=1&pt=0&bo=4AEOAQAAAAACd70!&tl=1&vuin=2292380798&tm=1597590000&t=5#sce=14-1-1&rf=v1_ht5_qz_3.4.0_001_idc_b-4-0" w="0" h="0" /><title></title><summary></summary></item><item layout="6" advertiser_id="0" aid="0"><summary size="300" color="#EAFA04">神奇清屏专用</summary><hr hidden="false" style="15" /></item><source name="" icon="" action="" appid="-1" /></msg>]'
xml_msg5 = '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
'<msg serviceID="1">'
'<item layout="4">'
'<title>神奇666</title>'
'<picture cover="https://python3student.github.io/img/top.jpg"/>'
'</item>'
'</msg>]'
resp_dict5 = {'msg_type': 'group', 'number': 1143107466,
              'msg': '[CQ:xml,data=<?xml version="1.0" encoding="UTF-8" standalone="yes" ?><msg serviceID="2" '
                     'templateID="1" action="web" brief="" sourceMsgId="0" url="https://qm.qq.com/cgi-bin/qm/qr?k=wyw10nH14NxBzBmM2DZK_bj9y9yX-IJL" '
                     'flag="0" adverSign="0" multiMsgFlag="0"><item layout="2"><audio '
                     'cover="http://p4.music.126.net/88n5fQJCS69veHsSbpOc6Q==/109951166490429711.jpg?param=320y320" '
                     'src="http://music.163.com/song/media/outer/url?id=1884207046" '
                     '/><title>花小楼-你可不可以跟我看一看彩虹（星灵/K-987 Remix）</title><summary>『作者』陌漓-Molly</summary></item><source name="神奇永远的神！" '
                     'icon="https://qlogo3.store.qq.com/qzone/469784630/469784630/100?1644649703" '
                     'url="https://qlogo3.store.qq.com/qzone/469784630/469784630/100?1644649703ttps://python3student.github.io/img/avatar.jpg" action="app" '
                     'a_actionData="com.netease.cloudmusic" i_actionData="tencent100495085://" appid="100495085" '
                     '/></msg>,resid=60]'}

# https://music.163.com/song/media/outer/url?id=28613172.mp3
# send_msg(resp_dict3)
# send_msg(resp_dict2)
# for i in range(5):
#     send_msg(resp_dict)
# get_group(543303513)
# send_msg(card)
# for i in range(400):
#     face['msg'] = face['msg'].format(i)
#     send_msg(face)
#     face = {'msg_type': 'group', 'number': 424714996, 'msg': '[CQ:face,id={}]'}
# send_msg(ban)
# send_msg(resp_dict1)
# send_msg({'msg_type': 'private', 'number': 1662941153,
#           'msg': xml_msg5})
# send_msg(resp_dict5)
# 清大文森
# for _ in range(10):
#     send_msg({'msg_type': 'group', 'number': 543303513,
#               'msg': '签到'})

# mch
# http://miniapp.gtimg.cn/public/appicon/432b76be3a548fc128acaa6c1ec90131_200.jpg
# https://qlogo1.store.qq.com/qzone/1642883508/1642883508/100?1656072797
# mch = '[CQ:json,data={"app":"com.tencent.miniapp_01"&#44;"config":{' \
#       '"autoSize":0&#44;"ctime":1657275643&#44;"forward":1&#44;"height":0&#44;"token' \
#       '":"ebaecae9221e4944e2dcabc61cbc6017"&#44;"type":"normal"&#44;"width":0}&#44;"desc":"哔哩哔哩"&#44;"extra":{' \
#       '"app_type":1&#44;"appid":100951776&#44;"uin":1642883508}&#44;"meta":{"detail_1":{' \
#       '"appType":0&#44;"appid":"1109937557"&#44;"desc":"《好友列表都去做谢军敏二创了没人陪我打云顶》"&#44;"gamePoints":""&#44' \
#       ';"gamePointsUrl":""&#44;"host":{"nick":"铭记510"&#44;"uin":1642883508}&#44;"icon":"http://miniapp.gtimg.cn' \
#       '/public/appicon/432b76be3a548fc128acaa6c1ec90131_200.jpg"&#44;"preview":"pubminishare-30161.picsz.qpic.cn' \
#       '/147d3fbd-9a2a-4c39-8e60-89d58b86c537"&#44;"qqdocurl":"https://b23.tv/0UPZLNI?share_medium=android&amp' \
#       ';share_source=qq&amp;bbid=XY07A1F0D5AD2FF00771E997C25A66B45CB86&amp;ts=1657275637100"&#44;"scene":1036&#44' \
#       ';"shareTemplateData":{}&#44;"shareTemplateId":"8C8E89B49BE609866298ADDFF2DBABA4"&#44;"showLittleTail":""&#44' \
#       ';"title":"哔哩哔哩"&#44;"url":"m.q.qq.com/a/s/f45f3a1c2d403ae4ad54f948a0d352f7"}}&#44;"needShareCallBack":false' \
#       '&#44;"prompt":"&#91;QQ小程序&#93;哔哩哔哩"&#44;"ver":"1.0.0.19"&#44;"view":"view_8C8E89B49BE609866298ADDFF2DBABA4"}] '
# send_msg({'msg_type': 'group', 'number': 1143107466,
#           'msg': mch})

# python自学交流群
# send_msg({'msg_type': 'group', 'number': 566077032,
#           'msg': '[CQ:tts,text=up主可以试试使用旋转法证明这个更一般的定理：对于圆锥曲线的一般方程，其中ABC不同时为0，令判别式，如果<0则曲线表示椭圆，=0表示抛物线，>0表示双曲线]'})
# mch
# send_msg({'msg_type': 'group', 'number': 1143107466,
#           'msg': '[CQ:tts,text=What are you barking for?]'})

# python自学交流群

# send_msg({'msg_type': 'group', 'number': 762093001,
#           'msg': '[CQ:record,file=http://music.163.com/song/media/outer/url?id=31365604.mp3]'})

# python自学交流群
# for i in range(1):
#     send_msg({'msg_type': 'group', 'number': 566077032,
#               'msg': '[CQ:record,file=http://music.163.com/song/media/outer/url?id=31365604.mp3]'})
#     send_msg({'msg_type': 'group', 'number': 566077032,
#               'msg': '音乐'})

_id = [31365604, 449818326, 548252595, 28613172, 27896762, 1873321491, 36990266]
music_lis = '[CQ:record,file=http://music.163.com/song/media/outer/url?id={}.mp3]'
# for id in _id:
#     send_msg({'msg_type': 'group', 'number': 1143107466,
#               'msg': msg.format(id)})
#     time.sleep(1)
# send_msg({'msg_type': 'group', 'number': 424714996,
#           'msg': music_lis.format(28613172)})
# 最伟大的作品 https://res.wx.qq.com/voice/getvoice?mediaid=MzIxOTM0NjA3N18xMDAwMDQ2NDE=.mp3
mus1 = '[CQ:record,file=http://music.163.com/song/media/outer/url?id={}.mp3]'
mus2 = '[CQ:record,file=https://res.wx.qq.com/voice/getvoice?mediaid=MzIxOTM0NjA3N18xMDAwMDQ2NDE=.mp3]'
mus3 = r'[CQ:record,file=file:/D:/WorkSpace/PC/_pygame/Seve.mp3]'
mus4 = r'[CQ:record,file=file:/D:/WorkSpace/PC/_pygame/z.mp3]'

# send_msg({'msg_type': 'group', 'number': 643272204,
#           'msg': mus1.format(28613172)})

# v1 = '[CQ:video,file=http://vfx.mtime.cn/Video/2019/03/18/mp4/190318231014076505.mp4]'
# send_msg({'msg_type': 'group', 'number': 1055277728,
#           'msg': mus4})
mus5 = r'[CQ:record,file=file:/D:/WorkSpace/PC/机器人/None_QQ/kaptreebot/yuyinbao/晚上好QQ：29835663.mp3]'
mus6 = '[CQ:record,file=A9D6E4E616DE774E9F780C5A31182B1F.amr]'
send_msg({'msg_type': 'group', 'number': 566077032,
          'msg': mus5})

# send_msg({'msg_type': 'private', 'number': 1692851288,
#           'msg': mus5})
# zidong
# zidong = '[CQ:json,data={"app":"com.tencent.gamecenter.gameshare"&#44;"desc":""&#44;"view":"noDataView"&#44;"ver":"0.0.0.0"&#44;"prompt":""&#44;"appID":""&#44;"sourceName":""&#44;"actionData":""&#44;"actionData_A":""&#44;"sourceUrl":""&#44;"meta":{"shareData":{"scene":"SCENE_SHARE_VIDEO"&#44;"jumpUrl":"https:\/\/m7.music.126.net\/20200718135354\/bbfc5f8a0639d1c2113489032f9067a9\/ymusic\/4fa5\/a2b6\/8659\/ee74ab310f636428356429c37b10767b.mp3"&#44;"type":"video"&#44;"url":"https:\/\/game.gtimg.cn\/images\/yxzj\/cp\/a20170915diaucharn\/bg.mp3"}}&#44;"config":{"forward":1}&#44;"text":""&#44;"extraApps":&#91;&#93;&#44;"sourceAd":""&#44;"extra":""}]'
# send_msg({'msg_type': 'group', 'number': 566077032,
#           'msg': zidong})
# cardimage1 = r'[CQ:cardimage,file=file:/D:\WorkSpace\PC\aaa_qrcode.png]'
# send_msg({'msg_type': 'group', 'number': 566077032,
#           'msg': cardimage1})
# send_msg({'msg_type': 'group', 'number': 748820990,
#           'msg': mus1.format(36990266)})


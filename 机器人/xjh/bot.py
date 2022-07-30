from receive import rev_msg
from send_msg import send_msg
import socket
import requests
import random
import urllib.request,json




guanwang = {'python' : 'https://www.python.org/',
            'CSDN':'https://www.csdn.net/',
            'csdn':'https://www.csdn.net/',
            '百度':'https://www.baidu.com/',
            'Bing':'https://cn.bing.com/',
            '谷歌':'https://www.google.com/',
            '360搜索':'https://www.so.com/',
            'Lightly':'https://lightly.teamcode.com/',
            '微信':'https://weixin.qq.com/',
            'QQ':'https://im.qq.com/index',
            'python 3.11.0':'https://www.python.org/ftp/python/3.11.0/python-3.11.0b4.exe',
            'python win7':'https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe',
            'python windows7':'https://www.python.org/ftp/python/3.8.10/python-3.8.10.exe',
            'Python' : 'https://www.python.org/',
            '西瓜博客': 'www.314669.xyz',
            '鸽子':'www.imfmkli.top',
            '小途智能': 'https://yyds666.icoc.ws/',
            '腾讯': 'https://www.tencent.com/zh-cn/',
            '360安全卫士': 'https://weishi.360.cn/',
            '金山办公': 'https://www.wps.cn/',
            '网易有道': 'https://www.youdao.com/',
            '4399':'https://www.4399.com/?hao360a'}




gongneng = '''
[CQ:face,id=138]功能：[CQ:face,id=138]
       1.签到
       2.查询官网(例：官网 python)
       3.发送语音(例：发送语音 大家好)
       4.物流查询(例：物流查询 韵达快递 3926978083099)
       5.官网入库（例：官网入库 百度(加号)+https://www.baidu.com/）
       6.发送音乐（例 ：音乐）
       7.网易点歌（例 ：网易点歌 孤勇者）
       8.手机号码归属地查询（例：手机号码归属地查询 138xxxxxxxx）
       9.天气查询（例：天气 上海）
       10.垃圾分类（例：垃圾分类 餐巾纸）
'''

cishu = 25

qunliao={818886947: 11, 858631271: 39, 712015138: 131}

siliao= {2369991281: 13, 1369363236: 23}

yiqiandao = {3567216550: '1', 2369991281: '1', 1369363236: '1', 1140585060: '1', 931234854: '1'}

qiandao = {1369363236: 3, 3567216550: 3, 3198357514: 1, 3312325389: 3, 2025138508: 1, 2511564293: 1, 3475602281: 1, 931234854: 2, 848135971: 1, 2369991281: 2, 1140585060: 2, 1625924030: 1, 1931743640: 1}
xiaoxi = {}

while True:
    a = '群聊\n'+str(qunliao)+'\n私聊\n' +str(siliao)+'\n今日已签到\n'+str(yiqiandao)+'\n签到详情\n'+str(qiandao)+'\n官网'+str(guanwang)
    a1 = open('字典.txt','w')
    a1.write(a)
    a1.close()
    try:
        rev = rev_msg()
        if rev["post_type"] != 'meta_event':
            print(rev)
            print('\n')
        if rev == None:
            continue
    except:
        continue

    
    if rev["post_type"] == "message":
        if rev["message_type"] == "private": #私聊

            
            if '傻逼' in rev['raw_message'] or 'sb' in rev['raw_message'] or '伞兵' in rev['raw_message'] or '智，障' in rev['raw_message'] or '笨' in rev['raw_message'] or 'SB' in rev['raw_message'] or '智障' in rev['raw_message'] or '艹' in rev['raw_message'] or 'md' in rev['raw_message'] or 'MD' in rev['raw_message'] or '妈的' in rev['raw_message']:
                qq=rev['sender']['user_id']
                
                if qq in siliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'您今日体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'不许骂人'})


            elif '官网入库' in rev['raw_message']:
                qq=rev['sender']['user_id']

                if qq in siliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'您今日体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    s1 = rev['raw_message']
                    s = len(s1)
                    b = -1
                    for i in s1:
                        b = b+1
                        if i=='+':
                            break
                    wangzhan = s1[5:b]
                    wangzhi = s1[b+1:s]
                    if wangzhan in guanwang:
                        send_msg({'msg_type':'private','number':qq,'msg':'此网站已被收录'})
                    else:
                        guanwang[wangzhan] = wangzhi
                        send_msg({'msg_type':'private','number':qq,'msg':'入库成功'})
                    


            elif '官网' in rev['raw_message']:
                d = len(rev['raw_message'])
                e = rev['raw_message'][3:d]
                qq=rev['sender']['user_id']

                if qq in siliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'您今日体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    if e in guanwang:
                        send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']'+ e+'的官网'+guanwang[e]})
                    else:
                        send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']'+ '对不起我还没有收录该网址,您可以进行入库，或者请用  官网 xxx  的格式发送(必输空格)'}) 
                
            elif '语音' in rev['raw_message']:
                qq=rev['sender']['user_id']

                if qq in siliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'您今日体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    d = len(rev['raw_message'])
                    e = rev['raw_message'][4:d]
                    send_msg({'msg_type':'private','number':qq,'msg':'[CQ:tts,text='+e+']'})


            elif '音乐' in rev['raw_message']:
                qq=rev['sender']['user_id']

                if qq in siliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'您今日体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    d = len(rev['raw_message'])
                    e = rev['raw_message'][4:d]
                    send_msg({'msg_type':'private','number':qq,'msg':'[CQ:record,file=http://music.163.com/song/media/outer/url?id=36990266.mp3]'})
                    
            elif '智能' in rev['raw_message']:
                qq=rev['sender']['user_id']

                if qq in siliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'您今日体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'谢谢夸奖'})


                    
            elif '功能' in rev['raw_message'] or '用处' in rev['raw_message']:
                qq=rev['sender']['user_id']
                
                if qq in siliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'您今日体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    send_msg({'msg_type':'private','number':qq,'msg':gongneng})

                    
            elif '签到' in rev['raw_message'] and '不' not in rev['raw_message'] or '签 到' in rev['raw_message']:
                qq=rev['sender']['user_id']

                if qq in siliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'您今日体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    if qq in yiqiandao:
                        send_msg({'msg_type':'private','number':qq,'msg':'今日已签到，明日再来！'})
                    else:
                        r = random.randint(0,10)
                        if r < 7 :
                            if qq in qiandao:
                                qiandao[qq] = qiandao[qq] + 1
                            else:
                                qiandao[qq] = 1
                            send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']签到成功\n已连续签到'+str(qiandao[qq])+'天，当前'+ str(qiandao[qq]) +'积分'})
                            yiqiandao[qq] = '1'
                        else :
                            send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']签到失败，请重试！'})


            elif '加油' in rev['raw_message']:
                qq=rev['sender']['user_id']

                if qq in siliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'您今日体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'我会努力的'})

            elif '物流查询' in rev['raw_message'] or '快递查询' in rev['raw_message']:

                qq=rev['sender']['user_id']
                if qq in qunliao:
                    qunliao[qq] = qunliao[qq]+3
                else:
                    qunliao[qq] =1
                if qunliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'您今日体验次数已达上限，不可再使用'})
                if qunliao[qq] < 21:


                    wuliu = """仅支持以下快递公司查询：
                    申通快递
                    EMS邮政
                    圆通快递
                    顺风快递
                    韵达快递
                    中通快递
                    天天快递
                    德邦物流
                    汇通快递
                    例：物流查询 韵达快递 3926978083099"""
                    
                    kd_dict = {1:'shentong',2:'youzhengguonei',3:'yuantong',4:'shunfeng',5:'yunda',6:'zhongtong',7:"tiantian",8:"debangwuliu",9:'huitongkuaidi'} 
                    
                    if '申通快递' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][10:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[1], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                send_msg({'msg_type':'private','number':qq,'msg':a+'\n'+b})
                        else:
                            send_msg({'msg_type':'private','number':qq,'msg':'查无此快递'})


                    elif 'EMS邮政' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][11:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[2], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                send_msg({'msg_type':'private','number':qq,'msg':a+'\n'+b})
                        else:
                            send_msg({'msg_type':'private','number':qq,'msg':'查无此快递'})

                    elif '圆通快递' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][10:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[3], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                send_msg({'msg_type':'private','number':qq,'msg':a+'\n'+b})
                        else:
                            send_msg({'msg_type':'private','number':qq,'msg':'查无此快递'})


                    elif '顺丰快递' in rev['raw_message'] or '顺风快递' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][10:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[4], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                send_msg({'msg_type':'private','number':qq,'msg':a+'\n'+b})
                        else:
                            send_msg({'msg_type':'private','number':qq,'msg':'查无此快递'})
                    

                    elif '韵达快递' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][10:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[5], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                send_msg({'msg_type':'private','number':qq,'msg':a+'\n'+b})
                        else:
                            send_msg({'msg_type':'private','number':qq,'msg':'查无此快递'})

                    
                    elif '中通快递' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][10:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[6], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                send_msg({'msg_type':'private','number':qq,'msg':a+'\n'+b})
                        else:
                            send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']查无此快递'})

                    
                    elif '天天快递' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][10:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[7], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                send_msg({'msg_type':'private','number':qq,'msg':a+'\n'+b})
                        else:
                            send_msg({'msg_type':'private','number':qq,'msg':'查无此快递'})
                        

                    elif '德邦快递' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][10:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[8], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                send_msg({'msg_type':'private','number':qq,'msg':a+'\n'+b})
                        else:
                            send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']查无此快递'})
                    
                    elif '汇通快递' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][10:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[9], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                send_msg({'msg_type':'private','number':qq,'msg':a+'\n'+b})
                        else:
                            send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']查无此快递'})
                        
                    else:
                        send_msg({'msg_type':'private','number':qq,'msg':wuliu})
            elif '天气' in rev['raw_message']:
                qq=rev['sender']['user_id']
                if qq in qunliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    if rev['raw_message'][0:3] != '天气 ':
                        send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']格式错误'})
                    else:
                        l = len(rev['raw_message'])
                        s = rev['raw_message'][3:l]
                        print(s)
                        if rev['raw_message'][0:3] != '天气 ':
                            send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']格式错误'})
                        else:
                            url = 'https://api.vvhan.com/api/weather?city='+s+'&type=week'
                            params = {}
                            params['area'] = ''
                            params['areaId'] = ''
                                
                                
                            headers = {
                                    
                                'Content-Type': 'application/json;charset=UTF-8',
                            }
                            r = requests.request("POST", url, params=params, headers=headers)
                            a = r.json()
                            if 'message' in a:
                                printsend_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']'+a['message']})
                            else:
                                b= a['data']
                                c = b['forecast']
                                d = c[0]#当日
                                e = c[1]#次日
                                g = c[2]
                                city = b['city']

                                date = d['date']
                                week = d['week']
                                tianqi = d['type']
                                high = '最'+d['high']
                                low = '最'+d['low']
                                fengxiang = d['fengxiang']
                                fengli = d['fengli']

                                date1 = e['date']
                                week1 = e['week']
                                tianqi1 = e['type']
                                high1 = '最'+e['high']
                                low1= '最'+e['low']
                                fengxiang1 = e['fengxiang']
                                fengli1 = e['fengli']

                                date2 = g['date']
                                week2 = g['week']
                                tianqi2 = g['type']
                                high2 = '最'+g['high']
                                low2= '最'+g['low']
                                fengxiang2 = g['fengxiang']
                                fengli2 = g['fengli']

                                f = city+':\n'+'\n'+date+' '+week+'\n'+tianqi+'\n'+high+'\n'+low+'\n'+fengxiang+'\n'+fengli+'\n'+'\n'+date1+''+week1+'\n'+tianqi1+'\n'+high1+'\n'+low1+'\n'+fengxiang1+'\n'+fengli1+'\n''\n'+date2+''+week2+'\n'+tianqi2+'\n'+high2+'\n'+low2+'\n'+fengxiang2+'\n'+fengli2  
                                send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']\n'+f})
            elif '音乐' in rev['raw_message']:
                qq=rev['sender']['user_id']
                if qq in siliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'您今日机器人体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    yinyue = ['http://music.163.com/song/media/outer/url?id=36990266.mp3',
                              'http://m10.music.126.net/20220729093654/f10912cf255f0f643d4dc27fdf116107/ymusic/cd83/7084/b9e6/381d04785de4b1984543f24bdfdad802.mp3',
                              'http://m10.music.126.net/20220729094007/7c32007dff22919165ec9fe5dbcaae29/ymusic/ffdb/183c/8bf3/46ede7216e3c6f14404da66d8da02b27.mp3',
                              'http://m701.music.126.net/20220729100417/dbf9e39c82f34b0a18c0048c4cf1ea43/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/14096431035/6899/efc1/4dc9/8f476229e0759cfda5e2c6c7d18c58da.mp3',
                              'http://music.163.com/song/media/outer/url?id=1901371647.mp3',
                              'http://music.163.com/song/media/outer/url?id=1958357679.mp3',
                              'http://music.163.com/song/media/outer/url?id=1815085049.mp3',
                              'http://music.163.com/song/media/outer/url?id=1804320463.mp3',
                              'http://music.163.com/song/media/outer/url?id=1892668095.mp3',
                              'http://music.163.com/song/media/outer/url?id=1967457117.mp3',
                              'http://music.163.com/song/media/outer/url?id=1965648349.mp3']
                    s = random.randint(0,2)
                    send_msg({'msg_type':'private','number':qq,'msg':'[CQ:record,file='+yinyue[s]+']'})

            elif '网易点歌' in rev['raw_message']:
                qq=rev['sender']['user_id']
                if qq in siliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'group','private':qq,'msg':'您今日机器人体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    yinyue = {'孤勇者':'http://music.163.com/song/media/outer/url?id=1901371647.mp3',
                               '听我说谢谢你':'http://music.163.com/song/media/outer/url?id=1958357679.mp3',
                               '雾里':'http://music.163.com/song/media/outer/url?id=1815085049.mp3',
                               '踏山河':'http://music.163.com/song/media/outer/url?id=1804320463.mp3',
                               '你叉叉':'http://music.163.com/song/media/outer/url?id=1892668095.mp3',
                               '不得不撒':'http://music.163.com/song/media/outer/url?id=1967457117.mp3',
                               '周周':'http://music.163.com/song/media/outer/url?id=1965648349.mp3'}
                    s = len(rev['raw_message'])
                    s = rev['raw_message'][5:s]
                    if s in yinyue:
                        send_msg({'msg_type':'private','number':qq,'msg':'[CQ:record,file='+yinyue[s]+']'})
                    else:
                        zhichi= '''目前支持：
                                   孤勇者
                                   听我说谢谢你
                                   雾里
                                   踏山河
                                   你叉叉
                                   不得不撒'''
                        send_msg({'msg_type':'private','number':qq,'msg':'很抱歉我还没有收录该歌曲，您可以联系邢佳豪\n'+zhichi})

    
                    
            elif '你好' in rev['raw_message']:
                d = ['你好','HI','[CQ:face,id=119]']
                r = random.randint(0,2)
                qq=rev['sender']['user_id']

                if qq in siliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'您今日体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    send_msg({'msg_type':'private','number':qq,'msg':d[r]})

                    
            elif '睡觉' in rev['raw_message'] or '睡眠' in rev['raw_message'] or '睡吧' in rev['raw_message'] or '晚安' in rev['raw_message']:
                qq=rev['sender']['user_id']
                
                if qq in siliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'您今日体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'晚安'})
                    
            elif '垃圾分类' in rev['raw_message']:
                qq=rev['sender']['user_id']
                if qq in qunliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    l = len(rev['raw_message'])
                    s = rev['raw_message'][5:l]
                    if rev['raw_message'][0:5] != '垃圾分类 ':
                        send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']格式错误'})
                    else:
                        url = 'https://api.vvhan.com/api/la.ji?lj='+s
                        params = {}
                        params['area'] = ''
                        params['areaId'] = ''
                            
                            
                        headers = {
                                
                            'Content-Type': 'application/json;charset=UTF-8',
                        }
                        r = requests.request("POST", url, params=params, headers=headers)
                        a = r.json()
                        if a['success'] == False:
                            send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']输入错误'})
                        else:
                            b = a['name']+':'
                            c = a['sort']
                            send_msg({'msg_type':'private','number':qq,'msg':'[CQ:at,qq='+str(qq)+']'+b+c})
                    
            elif '在' in rev['raw_message']:
                d = ['我在','在呢','我当然在']
                r = random.randint(0,2)
                qq=rev['sender']['user_id']

                if qq in siliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'您今日体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    send_msg({'msg_type':'private','number':qq,'msg':d[r]})

                    
            elif '关闭' in rev['raw_message'] or '退出' in rev['raw_message'] or '关机' in rev['raw_message']:
                qq=rev['sender']['user_id']

                if qq in siliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'您今日体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    if qq == 3567216550: 
                        send_msg({'msg_type':'private','number':qq,'msg':'已关闭'})
                        break
                    else:
                        send_msg({'msg_type':'private','number':qq,'msg':'对不起，您无权限'})
            else:
                qq=rev['sender']['user_id']
                
                if qq in siliao:
                    siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
                if siliao[qq] == 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'您今日体验次数已达上限，不可再使用'})
                if siliao[qq] < 21:
                    send_msg({'msg_type':'private','number':qq,'msg':'对不起我不会'})





                    
        elif rev["message_type"] == "group": #群聊
            group = rev['group_id']

            fch = rev['raw_message']
            
            if '傻逼' in rev['raw_message'] or 'sb' in rev['raw_message']or '伞兵' in rev['raw_message']  or '笨' in rev['raw_message'] or 'SB' in rev['raw_message'] or '智，障' in rev['raw_message'] or '艹' in rev['raw_message'] or '智障' in rev['raw_message']:
                qq=rev['sender']['user_id']
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+1
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']不许骂人'})


            elif '官网入库' in rev['raw_message']:
                qq=rev['sender']['user_id']
                
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+1
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:
                    s1 = rev['raw_message']
                    s = len(s1)
                    b = -1
                    for i in s1:
                        b = b+1
                        if i=='+':
                            break
                    wangzhan = s1[5:b]
                    wangzhi = s1[b+1:s]
                    if wangzhan in guanwang:
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']此网站已被收录'})
                    else:
                        guanwang[wangzhan] = wangzhi
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']入库成功'})

            elif '官网' in rev['raw_message']:
                qq=rev['sender']['user_id']
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+1
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:
                    d = len(rev['raw_message'])
                    e = rev['raw_message'][3:d]
                    if e in guanwang:
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']'+e+'的官网'+ guanwang[e]})
                    else:
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']'+ '对不起我还没有收录该网址，或者请用  官网 xxx  的格式发送(必输空格)'})

       
            elif '语音' in rev['raw_message']:
                qq=rev['sender']['user_id']
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+1
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:
                    d = len(rev['raw_message'])
                    e = rev['raw_message'][4:d]
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']'})
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:tts,text='+e+']'})
                    
            elif '智能' in rev['raw_message']:
                qq=rev['sender']['user_id']
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+1
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']谢谢夸奖'})

            elif '垃圾分类' in rev['raw_message']:
                qq=rev['sender']['user_id']
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+1
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:
                    l = len(rev['raw_message'])
                    s = rev['raw_message'][5:l]
                    if rev['raw_message'][0:5] != '垃圾分类 ':
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']格式错误'})
                    else:
                        url = 'https://api.vvhan.com/api/la.ji?lj='+s
                        params = {}
                        params['area'] = ''
                        params['areaId'] = ''
                            
                            
                        headers = {
                                
                            'Content-Type': 'application/json;charset=UTF-8',
                        }
                        r = requests.request("POST", url, params=params, headers=headers)
                        a = r.json()
                        if a['success'] == False:
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']输入错误'})
                        else:
                            b = a['name']+':'
                            c = a['sort']
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']'+b+c})
            elif '天气' in rev['raw_message']:
                qq=rev['sender']['user_id']
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+1
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:
                    l = len(rev['raw_message'])
                    s = rev['raw_message'][3:l]
                    if rev['raw_message'][0:3] != '天气 ':
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']格式错误'})
                    else:
                        url = 'https://api.vvhan.com/api/weather?city='+s+'&type=week'
                        params = {}
                        params['area'] = ''
                        params['areaId'] = ''
                            
                            
                        headers = {
                                
                            'Content-Type': 'application/json;charset=UTF-8',
                        }
                        r = requests.request("POST", url, params=params, headers=headers)
                        a = r.json()
                        if 'message' in a:
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']'+a['message']})
                        else:
                            b= a['data']
                            c = b['forecast']
                            d = c[0]#当日
                            e = c[1]#次日
                            g = c[2]
                            city = b['city']

                            date = d['date']
                            week = d['week']
                            tianqi = d['type']
                            high = '最'+d['high']
                            low = '最'+d['low']
                            fengxiang = d['fengxiang']
                            fengli = d['fengli']

                            date1 = e['date']
                            week1 = e['week']
                            tianqi1 = e['type']
                            high1 = '最'+e['high']
                            low1= '最'+e['low']
                            fengxiang1 = e['fengxiang']
                            fengli1 = e['fengli']

                            date2 = g['date']
                            week2 = g['week']
                            tianqi2 = g['type']
                            high2 = '最'+g['high']
                            low2= '最'+g['low']
                            fengxiang2 = g['fengxiang']
                            fengli2 = g['fengli']

                            f = city+':\n'+'\n'+date+' '+week+'\n'+tianqi+'\n'+high+'\n'+low+'\n'+fengxiang+'\n'+fengli+'\n'+'\n'+date1+''+week1+'\n'+tianqi1+'\n'+high1+'\n'+low1+'\n'+fengxiang1+'\n'+fengli1+'\n''\n'+date2+''+week2+'\n'+tianqi2+'\n'+high2+'\n'+low2+'\n'+fengxiang2+'\n'+fengli2  
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']\n'+f})
            elif '功能' in rev['raw_message'] or '用处' in rev['raw_message']:
                qq=rev['sender']['user_id']
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+1
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']' + gongneng})
                    
            elif '签到' in rev['raw_message'] or '签 到' in rev['raw_message'] and '不' not in rev['raw_message']:
                qq=rev['sender']['user_id']
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+1
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:
                    if qq in yiqiandao:
                        send_msg({'msg_type':'group','number':group,'msg':'今日已签到，明日再来！'})
                    else:
                        r = random.randint(0,10)
                        if r < 7 :
                            if qq in qiandao:
                                qiandao[qq] = qiandao[qq] + 1
                            else:
                                qiandao[qq] = 1
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']签到成功\n已连续签到'+str(qiandao[qq])+'天，当前'+ str(qiandao[qq]) +'积分'})
                            yiqiandao[qq] = '1'
                        else :
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']签到失败，请重试！'})




            elif '物流查询' in rev['raw_message'] or '快递查询' in rev['raw_message']:

                qq=rev['sender']['user_id']
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+7
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:


                    wuliu = """仅支持以下快递公司查询：
                    申通快递
                    EMS邮政
                    圆通快递
                    顺风快递
                    韵达快递
                    中通快递
                    天天快递
                    德邦物流
                    汇通快递
                    例：物流查询 韵达快递 3926978083099"""

                    c = '查询结果\n'
                    
                    kd_dict = {1:'shentong',2:'youzhengguonei',3:'yuantong',4:'shunfeng',5:'yunda',6:'zhongtong',7:"tiantian",8:"debangwuliu",9:'huitongkuaidi'} 
                    
                    if '申通快递' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][10:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[1], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                send_msg({'msg_type':'group','number':group,'msg':a+'\n'+b})
                        else:
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']查无此快递'})


                    elif 'EMS邮政' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][11:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[2], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                send_msg({'msg_type':'group','number':group,'msg':a+'\n'+b})
                        else:
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']查无此快递'})

                    elif '圆通快递' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][10:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[3], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                send_msg({'msg_type':'group','number':group,'msg':a+'\n'+b})
                        else:
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']查无此快递'})


                    elif '顺丰快递' in rev['raw_message'] or '顺风快递' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][10:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[4], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                send_msg({'msg_type':'group','number':group,'msg':a+'\n'+b})
                        else:
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']查无此快递'})
                    

                    elif '韵达快递' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][10:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[5], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                c = c+a+'\n'+b+'\n'
                            send_msg({'msg_type':'group','number':group,'msg':c})
                        else:
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']查无此快递'})

                    
                    elif '中通快递' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][10:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[6], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                send_msg({'msg_type':'group','number':group,'msg':a+'\n'+b})
                        else:
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']查无此快递'})

                    
                    elif '天天快递' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][10:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[7], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                send_msg({'msg_type':'group','number':group,'msg':a+'\n'+b})
                        else:
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']查无此快递'})
                        

                    elif '德邦快递' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][10:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[8], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                send_msg({'msg_type':'group','number':group,'msg':a+'\n'+b})
                        else:
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']查无此快递'})
                    
                    elif '汇通快递' in rev['raw_message']:
                        chang = len(rev['raw_message'])
                        kd_num =  rev['raw_message'][10:chang]
                        url = "http://www.kuaidi100.com/query?type=%s&postid=%s" % (kd_dict[9], kd_num)
                        response = urllib.request.urlopen(url)
                        html = response.read().decode('utf-8')
                        target = json.loads(html)
                        status = target['status']
                        if status == '200':
                            data = target['data']
                            data_len = len(data)
                            for i in range(data_len):
                                a = "时间: " + data[i]['time']
                                b = "状态: " + data[i]['context'] + ""
                                send_msg({'msg_type':'group','number':group,'msg':a+'\n'+b})
                        else:
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']查无此快递'})
                        
                    else:
                        send_msg({'msg_type':'group','number':group,'msg':wuliu})
                        

            elif '你好' in rev['raw_message']:
                d = ['你好','HI','[CQ:face,id=119]']
                r = random.randint(0,2)
                qq=rev['sender']['user_id']
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+1
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']'+ d[r]})
            elif '加油' in rev['raw_message']:
                qq=rev['sender']['user_id']
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+1
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']我会努力的'})
            elif '睡觉' in rev['raw_message'] or '睡眠' in rev['raw_message'] or '睡吧' in rev['raw_message'] or '晚安' in rev['raw_message']:
                qq=rev['sender']['user_id']
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+1
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']晚安'})


            elif '在吗' in rev['raw_message']:
                d = ['我在','在呢','我当然在']
                r = random.randint(0,2)
                qq=rev['sender']['user_id']
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+1
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']'+ d[r]})

            elif '音乐' in rev['raw_message']:
                qq=rev['sender']['user_id']
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+1
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:
                    yinyue = ['http://music.163.com/song/media/outer/url?id=36990266.mp3',
                              'http://m10.music.126.net/20220729093654/f10912cf255f0f643d4dc27fdf116107/ymusic/cd83/7084/b9e6/381d04785de4b1984543f24bdfdad802.mp3',
                              'http://m10.music.126.net/20220729094007/7c32007dff22919165ec9fe5dbcaae29/ymusic/ffdb/183c/8bf3/46ede7216e3c6f14404da66d8da02b27.mp3',
                              'http://m701.music.126.net/20220729100417/dbf9e39c82f34b0a18c0048c4cf1ea43/jdymusic/obj/wo3DlMOGwrbDjj7DisKw/14096431035/6899/efc1/4dc9/8f476229e0759cfda5e2c6c7d18c58da.mp3',
                              'http://music.163.com/song/media/outer/url?id=1901371647.mp3',
                              'http://music.163.com/song/media/outer/url?id=1958357679.mp3',
                              'http://music.163.com/song/media/outer/url?id=1815085049.mp3',
                              'http://music.163.com/song/media/outer/url?id=1804320463.mp3',
                              'http://music.163.com/song/media/outer/url?id=1892668095.mp3',
                              'http://music.163.com/song/media/outer/url?id=1967457117.mp3',
                              'http://music.163.com/song/media/outer/url?id=1965648349.mp3']
                    s = random.randint(0,2)
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:record,file='+yinyue[s]+']'})

            elif '网易点歌' in rev['raw_message']:
                qq=rev['sender']['user_id']
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+1
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:
                    yinyue = {'孤勇者':'http://music.163.com/song/media/outer/url?id=1901371647.mp3',
                               '听我说谢谢你':'http://music.163.com/song/media/outer/url?id=1958357679.mp3',
                               '雾里':'http://music.163.com/song/media/outer/url?id=1815085049.mp3',
                               '踏山河':'http://music.163.com/song/media/outer/url?id=1804320463.mp3',
                               '你叉叉':'http://music.163.com/song/media/outer/url?id=1892668095.mp3',
                               '不得不撒':'http://music.163.com/song/media/outer/url?id=1967457117.mp3',
                               '周周':'http://music.163.com/song/media/outer/url?id=1965648349.mp3'}
                    s = len(rev['raw_message'])
                    s = rev['raw_message'][5:s]
                    if s in yinyue:
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:record,file='+yinyue[s]+']'})
                    else:
                        zhichi= '''目前支持：
                                   孤勇者
                                   听我说谢谢你
                                   雾里
                                   踏山河
                                   你叉叉
                                   不得不撒'''
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']很抱歉我还没有收录该歌曲，您可以联系[CQ:at,qq=3567216550]\n'+zhichi})
            elif '手机号码归属地查询' in rev['raw_message']:
                print(1)
                qq=rev['sender']['user_id']
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+1
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:
                    if '手机号码归属地查询' == rev['raw_message']:
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']格式错误'})
                    else:
                        a = len(rev['raw_message'])
                        s = rev['raw_message'][10:a]
                        if len(s) != 11:
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']格式错误'})
                        else:
                            url = 'https://hcapi02.api.bdymkt.com/mobile'
                            params = {}
                            params['mobile'] = s
                            headers = {'Content-Type': 'application/json;charset=UTF-8'
                                       ,'X-Bce-Signature': 'AppCode/05690097aa9643eaaad33f184e6caad1 '
                                       }
                            r = requests.request("GET", url, params=params, headers=headers)
                            a=r.json()
                            c = a['data']
                            d = c['city']+'\n'+c['types']
                            send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']查询结果：\n'+d})
            elif '关闭' in rev['raw_message'] or '退出' in rev['raw_message'] or '关机' in rev['raw_message']:
                qq=rev['sender']['user_id']
                qq2=rev['group_id']
                if qq2 in qunliao:
                    qunliao[qq2] = qunliao[qq2]+1
                else:
                    qunliao[qq2] =1
                if qunliao[qq2] == 1501:
                    send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                if qunliao[qq2] < 1501:
                    if qq == 3567216550: 
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']已关闭'})
                        break
                    else:
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']对不起，您无权限'})
            else:
                if '[CQ:at,qq=2234221054]' == rev['raw_message']:
                    d = ['你好','HI','[CQ:face,id=119]']
                    r = random.randint(0,2)
                    qq=rev['sender']['user_id']
                    qq2=rev['group_id']
                    if qq2 in qunliao:
                        qunliao[qq2] = qunliao[qq2]+1
                    else:
                        qunliao[qq2] =1
                    if qunliao[qq2] == 1501:
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                    if qunliao[qq2] < 1501:
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']' + d[r]})
                elif '[CQ:at,qq=2234221054]' in rev['raw_message']:
                    qq=rev['sender']['user_id']
                    qq2=rev['group_id']
                    if qq2 in qunliao:
                        qunliao[qq2] = qunliao[qq2]+1
                    else:
                        qunliao[qq2] =1
                    if qunliao[qq2] == 1501:
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq=all]本群今日机器人体验次数已达上限，不可再使用'})
                    if qunliao[qq2] < 1501:
                        send_msg({'msg_type':'group','number':group,'msg':'[CQ:at,qq='+str(qq)+']对不起我还不会'})

            fchid = rev['message_id']
            xiaoxi[fchid] = rev
            
        else:
           continue
    elif rev["post_type"] =='notice':
        if rev["notice_type"] == "group_recall":
            qq2=rev['group_id']
            id1=rev['message_id']
            if id1 in xiaoxi:
                chxx = xiaoxi[id1]
                send_msg({'msg_type':'group','number':chxx['group_id'],'msg':'[CQ:at,qq='+str(chxx['user_id'])+']撤回了一条消息\n' + chxx['message']})
            if qq2 in qunliao:
                qunliao[qq2] = qunliao[qq2]+1
            else:
                qunliao[qq2] =1  
        if rev["notice_type"] == "private_recall":
            if rev['message_id'] == fchid:
                id1=rev['message_id']
                if id1 in xiaoxi:
                    chxx = xiaoxi[id1]
                    send_msg({'msg_type':'private','number':chxx['user_id'],'msg':'你撤回了一条消息\n' + chxx['message']})
                qq=rev['user_id']
                if qq in siliao:
                        siliao[qq] = siliao[qq]+1
                else:
                    siliao[qq] =1
        if rev["notice_type"] == "group_ban":
            if rev['sub_type'] == "ban":
                qq1 = rev['operator_id']  #禁言者 
                qq2 = rev['user_id'] #背禁言者
                if rev['duration']<3600:
                    send_msg({'msg_type':'group','number':rev['group_id'],'msg':'恭喜恭喜，[CQ:at,qq='+str(qq2)+']被[CQ:at,qq='+str(qq1)+']禁言了'+str(int(rev['duration']/60))+'分钟'})
                
                elif rev['duration']>=3600 and rev['duration']<86400:
                    send_msg({'msg_type':'group','number':rev['group_id'],'msg':'恭喜恭喜，[CQ:at,qq='+str(qq2)+']被[CQ:at,qq='+str(qq1)+']禁言了'+str(int(rev['duration']/360))+'小时'})
                else:
                    send_msg({'msg_type':'group','number':rev['group_id'],'msg':'恭喜恭喜，[CQ:at,qq='+str(qq2)+']被[CQ:at,qq='+str(qq1)+']禁言了'+str(int(rev['duration']/86400))+'天'})

            if rev['sub_type'] == "lift_ban":
                qq1 = rev['operator_id']  #禁言者 
                qq2 = rev['user_id'] #背禁言者
                send_msg({'msg_type':'group','number':rev['group_id'],'msg':'恭喜恭喜，[CQ:at,qq='+str(qq2)+']被[CQ:at,qq='+str(qq1)+']解除禁言了'})
                

    else:  # rev["post_type"]=="meta_event":
        continue




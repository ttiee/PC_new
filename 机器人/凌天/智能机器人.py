#!/usr/bin/env python 3.7
# -*- coding: utf-8 -*-
# @Time    : 2022/7/17 23:18
# @Author  : 奕凌天
# @Site    : 智能机器人，主要实现文字聊天，语音聊天等功能
# @File    : 001.py
# @Software: PyCharm
# 参考文档：https://blog.csdn.net/paisen110/article/details/124359423

# 模块安装
"""
python.exe -m pip install --upgrade pip  升级pip工具
pip install pyaudio 安装pyaudio依赖包, 用于录音、生成wav文件，如果失败，下载whl再次安装即可
pip install baidu-aip 安装百度AI的sdk, 调用语音技术接口将音频识别为文本数据返回
pip install pyttsx3 安装pyttsx3依赖包, 将文本信息以音频的格式播放出来
pip install chardet
"""

# 模块引用
import requests
import json
import time
import wave
import urllib
import pyttsx3
from aip import AipSpeech
from pyaudio import PyAudio, paInt16


# 接收用户的语音输入，并将其存为音频文件
framerate = 16000  # 采样率
num_samples = 2000  # 采样点
channels = 1  # 声道
sampwidth = 2  # 采样宽度2bytes
FILEPATH = '.\myvoices.wav'  # 该文件目录要存在

# 接收文本消息，调用百度UNIT智能机器人，回复文本消息
def get_data(sya):
    access_token = '24.8ae617c9be3d5810152384b8e47d3be5.2592000.1660661260.282335-26727598'
    url = 'https://aip.baidubce.com/rpc/2.0/unit/service/v3/chat?access_token=' + access_token
    post_data = {
        "version": "3.0",
        "service_id": "S72336",
        "session_id": " ",
        "log_id": "7758521",
        "request": {"terminal_id": "88888",
                    "query": sya}
        }

    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(url, json=post_data, headers=headers)
    data = response.json()['result']['responses'][0]['actions'][0]['say']

    return data

# 用于接收用户的语音输入, 并生成wav音频文件(wav、pcm、mp3的区别可详情百度)
class Speak():
    # 将音频数据保存到wav文件之中
    def save_wave_file(self, filepath, data):
        wf = wave.open(filepath, 'wb')
        wf.setnchannels(channels)
        wf.setsampwidth(sampwidth)
        wf.setframerate(framerate)
        wf.writeframes(b''.join(data))
        wf.close()

    # 进行语音录制工作
    def my_record(self):
        pa = PyAudio()
        # 打开一个新的音频stream
        stream = pa.open(format=paInt16, channels=channels,
                         rate=framerate, input=True, frames_per_buffer=num_samples)
        my_buf = []  # 存放录音数据

        t = time.time()
        print('正在讲话...')

        while time.time() < t + 5:  # 设置录音时间（秒）
            # 循环read，每次read 2000frames
            string_audio_data = stream.read(num_samples)
            my_buf.append(string_audio_data)

        print('讲话结束')
        self.save_wave_file(FILEPATH, my_buf)  # 保存下录音数据
        stream.close()



# APPID AK SK，调用接口, 调用BaiDu AI 接口进行录音、语音识别
APP_ID = '26722613'
API_KEY = 'f3GryGEBpaMNsPrEmss6EZi6'
SECRET_KEY = '81lLNwuGbAX7ywZrCY9QwQZ1TfGk8bZV'  # 此处填写自己的密钥
client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

class ReadWav():
    # 读取文件
    def get_file_content(self, filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    def predict(self):
        # 调用百度AI的接口, 识别本地文件
        data = self.get_file_content(FILEPATH)
        return client.asr(data, 'wav', 16000, {'dev_pid': 1537, })


# readWav = ReadWav()          #实例化方法
# print(readWav.predict())      #调用识别方法, 并输出


# 请求智能机器人, 发送文本信息, 调用青云客API接口，返回智能聊天内容
def talkWithRobot(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.parse.quote(msg))
    html = requests.get(url)
    return html.json()["content"]

# print(talkWithRobot("你好呀!"))


# 将回答信息转化为语音文件并输出
class RobotSay():

    def __init__(self):
        # 初始化语音
        self.engine = pyttsx3.init()  # 初始化语音库

        # 设置语速
        self.rate = self.engine.getProperty('rate')
        self.engine.setProperty('rate', self.rate - 50)

    def say(self, msg):
        # 输出语音
        self.engine.say(msg)  # 合成语音
        self.engine.runAndWait()


# robotSay = RobotSay()
# robotSay.say("你好呀")          #会讲出    ~你好呀(女声)


# 主函数
if __name__ == '__main__':
    robotSay = RobotSay()
    speak = Speak()
    readTalk = ReadWav()
    while True:
        speak.my_record()  # 录音
        text = readTalk.predict()['result'][0]  # 调用百度AI接口, 将录音转化为文本信息

        if text != "退出。":
            print("本人说:", text)  # 输出文本信息
            # response_dialogue = talkWithRobot(text)  # 调用青云客机器人回答文本信息并返回
            response_dialogue = get_data(text)
            print("青云客说:", response_dialogue)  # 输出回答文本信息
            robotSay.say(response_dialogue)  # 播放回答信息
        else:
            exit()















# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/7/26 15:18
作者：神奇

功能:
运行条件:安装manimgl
"""


"""
ffmpeg -i sampleVideo.mp4 -vcodec copy –an  audioLess.mp4
ffmpeg -i audioLess.mp4 -i sampleAudio.mp3 -c copy output.mp4

ffplay output.mp4
也就是 将原有视频的音频消除 然后 加入新的音频。

"""

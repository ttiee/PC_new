# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/10/4 20:42
作者：神奇

功能:
运行条件:安装manimgl
"""


# with open(r"C:\Users\ujbhi\Desktop\SurfaceExample.mp4", 'rb') as f:
#     a = f.read()
# with open(r"C:\Users\ujbhi\Desktop\DARK_SOUND_1080P.mp4", 'rb') as p:
#     b = p.read()
#
# with open(r"C:\Users\ujbhi\Desktop\D.mp4", 'wb') as i:
#     i.write(b+a)

from moviepy.editor import VideoFileClip, concatenate_videoclips
a = r"C:\Users\ujbhi\Desktop\DARK_SOUND_1080P.mp4"
b = r"C:\Users\ujbhi\Desktop\SurfaceExample.mp4"
save_path = r"C:\Users\ujbhi\Desktop\D.mp4"

video1 = VideoFileClip(a)
video2 = VideoFileClip(b)
file_names = [video1, video2]
# 拼接视频
clip = concatenate_videoclips(file_names)

# 生成目标视频文件
clip.to_videofile(save_path, fps=24, remove_temp=False)

r'''
from moviepy.editor import VideoFileClip, concatenate_videoclips
import os

# 参数设置
data_path = './data'  # 分散视频路径
suffix = '.ts'  # 分散的视频后缀
save_path = "./合并结果.mp4"  # 合并后的视频名称

# 开始合并
file_names = []
for root, dirs, files in os.walk(data_path):
    # 按文件名排序
    files.sort()
    # 遍历所有文件
    for file in files:
        # 如果后缀名为 .mp4
        if os.path.splitext(file)[1] == suffix:
            # 拼接成完整路径
            filePath = os.path.join(root, file)
            # 载入视频
            video = VideoFileClip(filePath)
            # 添加到数组
            file_names.append(video)

# 拼接视频
clip = concatenate_videoclips(file_names)

# 生成目标视频文件
clip.to_videofile(save_path, fps=24, remove_temp=False)
'''
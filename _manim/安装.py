# -*- coding: UTF-8 -*-

"""
序号:001
功能:
运行条件:安装manim库
time=2022/07/24
author=神奇
"""

"""
安装
https://www.bilibili.com/read/cv3387999
https://www.bilibili.com/video/BV14i4y1G7Yr?share_source=copy_web&vd_source=eaaf08b876e72f2df9757517af627635
https://www.bilibili.com/video/BV1uM4y1c7Bc?share_source=copy_web&vd_source=eaaf08b876e72f2df9757517af627635

目录
manim简介 00:00
系统版本查看 00:17
安装Python 00:26
FFmpeg安装 00:59
dvisvgm安装 02:07
LaTeX安装 03:15
Sox安装 04:47
Pycairo安装 05:31
https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo
manim的最终安装 06:32
https://github.com/3b1b/manim
pip install -r requirements.txt



教程
https://www.bilibili.com/video/BV1W4411Z7Zt?share_source=copy_web&vd_source=eaaf08b876e72f2df9757517af627635
https://github.com/cai-hust/manim-tutorial-CN



pip install manimgl
manimgl example_scenes.py OpeningManimExample
manimgl --config

"""

"""
manimgl 安装.py SquareToCircle
manimgl 安装.py SquareToCircle -ow
"""

from manimlib import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)

        self.add(circle)


"""
# import manimlib
from manimlib import *
# from manim import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        square.flip(RIGHT)
        square.rotate(-3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(Create(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))
"""

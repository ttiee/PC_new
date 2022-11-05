# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/7/27 13:56
作者：神奇

功能:傅里叶级数
运行条件:安装manim

manim -pql scene.py CreateCircle
manim -pql 07.py CreateCircle
"""
from manim import *

r'''
from fourier_series import FourierCirclesScene


class FourierOfPiSymbol(FourierCirclesScene):
    CONFIG = {
        "n_vectors": 51,
        "center_point": ORIGIN,
        "slow_factor": 0.1,
        "n_cycles": 1,
        "tex": "\\pi",
        "start_drawn": False,
        "max_circle_stroke_width": 1,
    }
'''


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


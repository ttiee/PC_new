# -*- coding: UTF-8 -*-

"""
序号:002
功能:制作成动画
运行条件:安装manimgl
time=2022/07/25
author=神奇
教程：https://docs.manim.org.cn/getting_started/quickstart.html


manimgl 动画.py SquareToCircle
manimgl 动画.py SquareToCircle -ow
"""

from manimlib import *


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        circle.set_stroke(BLUE_E, width=4)
        square = Square()

        self.play(ShowCreation(square))
        self.wait()
        self.play(ReplacementTransform(square, circle))
        self.wait()
        # self.play(ShowCreation(circle))

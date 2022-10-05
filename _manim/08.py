# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/10/4 17:37
作者：神奇

功能:
运行条件:安装manimgl
"""
"""
manimgl 08.py M08

"""

from manimlib import *


class M08(Scene):
    def text1(self):
        t1 = Text('10篇文言文挖空训练', font='SimHei', color=BLUE_C).scale(1.5).scale(0.4).shift([-5.4, 3.5, 0])
        t3 = Text('by 神奇', font='SimHei', color=BLUE_D).scale(0.4).shift([-5.4, 3.5, 0])
        square1 = Square().scale(0.2).shift([-6.15, 3.5, 0]).set_color(BLUE_B)
        img = ImageMobject(r"C:\Users\ujbhi\Desktop\视频\C.png").scale(3)
        img1 = FadeIn(ImageMobject(r"C:\Users\ujbhi\Desktop\视频\1.jpg").scale(0.1).shift([-6.15, 3.5, 0]))


        self.add(img)
        t1.fix_in_frame()
        # t1.to_edge(UP)
        # t1.fix_in_frame()
        # t2.to_edge(UP)
        self.play(FadeIn(t1))
        self.wait(5)
        self.play(TransformMatchingShapes(t1, t3))
        self.play(ShowCreation(square1))
        self.play(img1)
        # self.play(FadeOut(square1, time=0.5))
        self.wait(5)

    def construct(self):
        self.text1()

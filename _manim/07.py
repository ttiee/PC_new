# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/9/10 17:52
作者：神奇

功能:
运行条件:安装manimgl
"""

"""
manimgl 07.py M07

"""

from manimlib import *


class M07(Scene):
    def text1(self):
        t1 = Text('大家好，我是神奇', font='SimHei').scale(1.5)
        t2 = Text('今天为大家演示几个函数', font='SimHei')
        t3 = Text('by 神奇', font='SimHei', color=BLUE_D).scale(0.4).shift([-5.4, 3.5, 0])
        square1 = Square().scale(0.2).shift([-6.15, 3.5, 0])
        img = FadeIn(ImageMobject(r"C:\Users\ujbhi\Desktop\视频\1.jpg").scale(0.1).shift([-6.15, 3.5, 0]))

        t1.fix_in_frame()
        # t1.to_edge(UP)
        # t1.fix_in_frame()
        # t2.to_edge(UP)
        self.play(FadeIn(t1))
        self.wait()
        self.play(TransformMatchingShapes(t1, t3))
        self.play(ShowCreation(square1))
        self.play(img)
        # self.play(FadeOut(square1, time=0.5))
        # self.wait(0.5)
        self.play(ShowCreation(t2))
        self.wait()
        self.play(FadeOut(t2))

    def an1(self) -> Axes:
        an = Axes(
            x_range=(-5, 5, 1),
            y_range=(-5, 5, 1),
            axis_config={
                "include_tip": False,
                "include_numbers": True,
                "numbers_to_exclude": [0],
            },
            x_axis_config={},
            y_axis_config={
                "line_to_number_direction": DOWN,
                'number_direction': UP,
            },
            height=FRAME_HEIGHT - 2,
            width=FRAME_WIDTH - 2,
        )
        # an.add_coordinate_labels()

        self.play(Write(an))
        # self.add(
        #     an.get_axis_label(
        #         label_tex='y',
        #         axis=UP,
        #         edge=UP,
        #         direction=UP,
        #     )
        # )
        return an

    def an2(self, an: Axes):
        def fun1(x):
            return 1/x
        function_1 = an.get_graph(
            fun1,
            x_range=[-5, 5],
            discontinuities=[0],
            color=BLUE,
        )

        def fun2(x):
            x1 = x**2 - 1
            return math.sqrt(x1) if x1 >= 0 else math.sqrt(-x1)
        function_2 = an.get_graph(
            fun2,
            x_range=[-5, 5],
            color=BLUE,
        )
        self.play(FadeIn(function_2))

    def construct(self):
        # self.text1()
        an = self.an1()
        self.an2(an=an)

# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/7/27 7:31
作者：神奇

功能:
运行条件:安装manimgl
"""

from manimlib.imports import *
from manimlib import *


class RedHeart(Scene):
    def construct(self):
    	self.add_sound("ManimPractice1BGMReflections.mp3")
        axes = Axes(x_min=-5, x_max=5, y_min=-3, y_max=4,
                    number_line_config={"unit_size": 1},
                    x_axis_config={"tick_frequency": 1})
        # 此处坐标上显示的是[-3,0][3,0][0,-3][0,3]
        axes.add_coordinates([-math.sqrt(8), math.sqrt(8)], [-math.sqrt(8), math.sqrt(8)])
        self.add(axes.get_axis_labels())
        self.play(Write(axes), Write(axes.axis_labels))
        heart_text = TextMobject(r"$f(x)=\left | x \right | ^{\frac{2}{3}}+0.9 \sqrt{8-x^{2}} \sin (\pi a x)$",
                                 color=YELLOW, font='Consolas').shift(DOWN * 3.5)
        self.play(Write(heart_text))
        heart_text.generate_target()
        heart_text.target.become(Text("I", color=YELLOW, font='Concolas')).shift(LEFT * 1.5)
        for a in {1, 3, 5, 7, 9, 11}:
            heart = ParametricFunction(
                lambda x: np.array([
                    x,
                    abs(x) ** (2 / 3) + 0.9 * math.sqrt(abs(8 - x ** 2)) * math.sin(PI * x * a),
                    0
                ]),
                t_min=-math.sqrt(8), t_max=math.sqrt(8)
            )
            a_text = Text("a = " + str(a), font='Concolas').shift(RIGHT * 4.5, UP * 3).scale(0.5)
            self.play(Write(a_text))
            self.play(ShowCreation(heart))
            if a != 11:
                self.play(FadeOut(heart), FadeOut(a_text))
            else:
                a_text.generate_target()
                a_text.target.become(Text("Manim...", font='Consolas')).shift(RIGHT * 3.375)
                self.play(FadeToColor(heart, RED), FadeOut(axes), FadeOut(axes.axis_labels))
                heart.generate_target()
                heart.target.become(Text("Love", color=RED, font='Consolas'))
                self.play(MoveToTarget(heart), MoveToTarget(heart_text), MoveToTarget(a_text))
                self.wait(2)


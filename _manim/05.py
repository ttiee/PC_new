# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/7/27 7:35
作者：神奇

功能:画函数
运行条件:安装manimgl
"""
from manimlib import *


class T1(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-1, 7, 1],
            y_range=[-2, 2, 1],
            width=8,
            height=4,
            axis_config={
                "include_tip": True,
            }
        )

        sin_graph = FunctionGraph(
            function=lambda x: np.sin(x),
            x_range=[0, 2 * np.pi, 0.1]
        )
        sin_graph.move_to(axes.get_origin(), aligned_edge=LEFT)

        self.play(Write(axes), run_time=1)
        self.play(Write(sin_graph), run_time=1)
        self.wait()


class T2(Scene):
    @staticmethod
    def circle(t):
        x = 2 * np.cos(t)
        y = 2 * np.sin(t)
        return np.array([x, y, 0.0])

    def construct(self):
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            width=8,
            height=6,
            axis_config={
                "include_tip": True,
            }
        )

        param_curve = ParametricCurve(
            t_func=self.circle,
            t_range=[0, 2 * np.pi, 0.05],
            color=GREEN,
        )

        self.play(Write(axes), run_time=1)
        self.play(Write(param_curve))
        self.wait()


class T3(Scene):
    @staticmethod
    def hyperbolic_curve(t):
        x = 1 / np.cos(t)
        y = np.tan(t)
        return np.array([x, y, 0.0])

    def construct(self):
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            width=6,
            height=6,
            axis_config={
                "include_tip": True,
            }
        )

        param_curve = ParametricCurve(
            t_func=self.hyperbolic_curve,
            t_range=[0, 2 * np.pi, 0.001],
            color=GREEN
        )

        v_group = Group(axes, param_curve)
        v_group.scale(0.8, about_point=ORIGIN)

        self.play(Write(axes), run_time=1)
        self.play(Write(param_curve))
        self.wait()


class M1(Scene):
    @staticmethod
    def circle(t):
        x = 2 * np.cos(t)
        y = 2 * np.sin(t)
        return np.array([x, y, 0.0])

    def construct(self):
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-3, 3, 1],
            width=8,
            height=6,
            axis_config={
                "include_tip": True,
            }
        )

        param_curve = ParametricCurve(
            t_func=self.circle,
            t_range=[0, 2 * np.pi, 0.05],
            color=GREEN,
        )

        self.play(Write(axes), run_time=1)
        self.play(Write(param_curve))
        # self.add_sound(r"D:\WorkSpace\PC\_manim\sound\Enler's Clock.mp3")
        self.wait()


class M3(Scene):
    def construct(self) -> None:
        self.add(NumberPlane())

        t = ValueTracker(0)
        d1 = Dot(np.array([t.get_value(), 1, 0]))
        d2 = Dot(np.array([-1, -1, 0]))

        line = DashedLine(np.array([t.get_value(), 1, 0]), d2).add_updater(lambda x: x.move_to([t.get_value(), 0, 0]))

        self.play(FadeIn(d1), FadeIn(d2), FadeIn(line))
        self.play(t.animate.set_value(5))

        # for _ in range(10):
        #     ...



# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/7/25 16:05
作者：神奇

功能:
运行条件:安装manimgl
"""
"""
manimgl 02.py M2
"""

from manimlib import *


class M2(Scene):
    def construct(self):
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

        axes = Axes((-3, 10), (-1, 8))
        axes.add_coordinate_labels()

        self.play(Write(axes, lag_ratio=0.01, run_time=2))

        # Axes.get_graph will return the graph of a function
        sin_graph = axes.get_graph(
            lambda x: 2 * math.sin(x),
            color=BLUE,
        )
        # By default, it draws it so as to somewhat smoothly interpolate
        # between sampled points (x, f(x)).  If the graph is meant to have
        # a corner, though, you can set use_smoothing to False
        relu_graph = axes.get_graph(
            lambda x: max(x, 0),
            use_smoothing=False,
            color=YELLOW,
        )
        # For discontinuous functions, you can specify the point of
        # discontinuity so that it does not try to draw over the gap.
        step_graph = axes.get_graph(
            lambda x: 2.0 if x > 3 else 1.0,
            discontinuities=[3],
            color=GREEN,
        )

        # Axes.get_graph_label takes in either a string or a mobject.
        # If it's a string, it treats it as a LaTeX expression.  By default
        # it places the label next to the graph near the right side, and
        # has it match the color of the graph
        # sin_label = axes.get_graph_label(sin_graph, "\\sin(x)")
        # relu_label = axes.get_graph_label(relu_graph, Text("ReLU"))
        # step_label = axes.get_graph_label(step_graph, Text("Step"), x=4)

        t4 = Tex(r'y = 2sin(x)').shift(UP + UP)

        self.play(
            ShowCreation(sin_graph),
            # FadeIn(sin_label, RIGHT),
        )
        self.play(ShowIncreasingSubsets(t4))
        self.wait(2)
        self.play(FadeOut(t4))

        # t5 = Text('分段函数', font='SimHei').shift(UP + UP)
        t5 = VGroup(Tex(r'x , x \textgreater 0'), Tex(r'0 ,  x \leq 0')).arrange(DOWN).shift(UP*3)
        y = Tex('y = ')
        y.next_to(t5, LEFT*2).shift(DOWN*0.05)
        brace = Brace(t5, LEFT)
        self.play(
            ReplacementTransform(sin_graph, relu_graph),
            # FadeTransform(sin_label, relu_label),
        )
        self.add(t5, brace, y)
        # self.play(ShowIncreasingSubsets(t5))
        self.wait(2)
        self.play(FadeOut(t5), FadeOut(y), FadeOut(brace))

        t6 = VGroup(Tex(r'2 , x \textgreater 3'), Tex(r'1 ,  x \leq 3')).arrange(DOWN).shift(UP*3)

        self.play(
            ReplacementTransform(relu_graph, step_graph),
            # FadeTransform(relu_label, step_label),
        )
        self.add(t6, brace, y)
        self.wait(2)
        self.play(FadeOut(t6), FadeOut(y), FadeOut(brace))

        t6 = Tex('y', '=', r'\frac{1}{4}x^2', font='SimHei').shift(RIGHT * 3)
        parabola = axes.get_graph(lambda x: 0.25 * x ** 2)
        parabola.set_stroke(GREEN_A)
        self.play(
            FadeOut(step_graph),
            # FadeOut(step_label),
            ShowCreation(parabola)
        )
        self.play(ShowIncreasingSubsets(t6))

        self.wait()

        # You can use axes.input_to_graph_point, abbreviated
        # to axes.i2gp, to find a particular point on a graph
        dot = Dot(color=RED)
        dot.move_to(axes.i2gp(2, parabola))
        self.play(FadeIn(dot, scale=0.5))

        # A value tracker lets us animate a parameter, usually
        # with the intent of having other mobjects update based
        # on the parameter
        x_tracker = ValueTracker(2)
        f_always(
            dot.move_to,
            lambda: axes.i2gp(x_tracker.get_value(), parabola)
        )

        self.play(x_tracker.animate.set_value(4), run_time=3)
        self.play(x_tracker.animate.set_value(-2), run_time=3)
        self.wait()


class t(Scene):
    def construct(self) -> None:
        self.add_sound(r"D:\WorkSpace\PC\_manim\sound\Enler's Clock.mp3")
        t1 = Tex('x^2')
        self.play(FadeIn(t1))
        self.wait()
        self.play(FadeOut(t1))
        # t2 = Tex(r'\left\{\begin{eqnarray}x_1+x_2+xx_3=-\frac{b}{a}\\x_1x_2+xx_2x_3+x_3x_1=\frac{c}{a}\\x_1x_2xx_3=-\frac{d}{a}\end{eqnarray}\right').shift(UP)
        # t2 = Tex(r'\Latex')
        t2 = Tex(r'\begin{aligned}A^2&=B^2+C^2\\A&=\sqrt{B^2+C^2}\end{aligned}')
        t3 = SingleStringTex(r'\begin{pmatrix}1&1\\1&1\end{pmatrix}')
        self.play(FadeIn(t2))
        self.wait()
        self.play(FadeOut(t2))
        self.play(FadeIn(t3))
        self.wait()
        self.play(FadeOut(t3))
        t4 = Tex(r'\sum_{i=1}^\infty\frac{1}{i^2}=\frac{\pi^2}{6}\\')
        self.play(FadeIn(t4))
        self.wait()
        self.play(FadeOut(t4))
        t5 = Tex(r' f(x)=\left\{\begin{aligned}x & =  \cos(t) \\y & =  \sin(t) \\z & =  \frac xy\end{aligned}\right.')
        self.play(FadeIn(t5))
        self.wait()
        # self.play(FadeOut(t5))




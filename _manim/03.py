# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/7/26 14:35
作者：神奇

功能:
运行条件:安装manimgl
"""

from manimlib import *


class Text_1(Scene):
    def construct(self):
        color_dict = {"A": BLUE, "B": YELLOW, "C": GREEN}
        split = ["A", "B", "C"]
        tex1 = Tex(
            r"A^2=B^2+C^2",
            font_size=80,
            isolate=split
        )
        tex2 = Tex(
            r"A=\sqrt{\,B^2+C^2 }",
            font_size=80,
            isolate=split
        )
        tex1.set_color_by_tex_to_color_map(color_dict)
        tex2.set_color_by_tex_to_color_map(color_dict)

        self.add(tex1)
        self.wait()
        self.play(ReplacementTransform(tex1, tex2), run_time=1)
        self.wait()


if __name__ == "__main__":
    from os import system

    system("manimgl {} Text_1".format(__file__))

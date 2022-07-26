# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/7/26 10:58
作者：神奇

功能:
运行条件:安装manimgl
"""

import os
from manimlib import get_tex_config


def dvi_to_svg(dvi_file, regen_if_exists=False):
    """
    Converts a dvi, which potentially has multiple slides, into a
    directory full of enumerated pngs corresponding with these slides.
    Returns a list of PIL Image objects for these images sorted as they
    where in the dvi
    """
    file_type = get_tex_config()["intermediate_filetype"]
    result = dvi_file.replace("." + file_type, ".svg")
    if not os.path.exists(result):
        commands = [
            "dvisvgm",
            "\"{}\"".format(dvi_file),
            "-n",
            "-v",
            "0",
            "-o",
            "\"{}\"".format(result),
            ">",
            os.devnull
        ]
        os.system(" ".join(commands))
    return result

r'''
dvisvgm "D:\WorkSpace\PC\_manim\1\Tex\34b9193f53b1fb0f.dvi" -n -v 0 -o "D:\WorkSpace\PC\_manim\1\Tex\34b9193f53b1fb0f.svg" > nul

mpm --register-components --verbose

https://www.bilibili.com/read/cv416707/
'''

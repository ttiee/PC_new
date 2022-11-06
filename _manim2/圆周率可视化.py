# -*- coding: UTF-8 -*-

"""
序号:001
时间：2022/11/5 15:48
作者：神奇

功能:
运行条件:安装manimgl
"""
from manim import *
import math


class PI_visualize(Scene):
    def construct(self):
        # 最外框每一段环形长度，颜色，内外半径设置
        # 代表十个数字的环形段顺时针排列
        angle_length = 32.0
        start_angles = (56, 20, -16, -52, -88, -124, -160, 164, 128, 92)
        colors = [DARK_BROWN, ORANGE, PURPLE_B, LIGHT_PINK, TEAL_B, BLUE_D, BLUE_E, BLUE_B, GREEN_E, GREEN_B]
        AS0 = AnnularSector(inner_radius=3.3, outer_radius=3.5, angle=angle_length * DEGREES,
                            start_angle=start_angles[0] * DEGREES, color=DARK_BROWN)
        AS1 = AnnularSector(inner_radius=3.3, outer_radius=3.5, angle=angle_length * DEGREES,
                            start_angle=start_angles[1] * DEGREES, color=ORANGE)
        AS2 = AnnularSector(inner_radius=3.3, outer_radius=3.5, angle=angle_length * DEGREES,
                            start_angle=start_angles[2] * DEGREES, color=PURPLE_B)
        AS3 = AnnularSector(inner_radius=3.3, outer_radius=3.5, angle=angle_length * DEGREES,
                            start_angle=start_angles[3] * DEGREES, color=LIGHT_PINK)
        AS4 = AnnularSector(inner_radius=3.3, outer_radius=3.5, angle=angle_length * DEGREES,
                            start_angle=start_angles[4] * DEGREES, color=TEAL_B)
        AS5 = AnnularSector(inner_radius=3.3, outer_radius=3.5, angle=angle_length * DEGREES,
                            start_angle=start_angles[5] * DEGREES, color=BLUE_D)
        AS6 = AnnularSector(inner_radius=3.3, outer_radius=3.5, angle=angle_length * DEGREES,
                            start_angle=start_angles[6] * DEGREES, color=BLUE_E)
        AS7 = AnnularSector(inner_radius=3.3, outer_radius=3.5, angle=angle_length * DEGREES,
                            start_angle=start_angles[7] * DEGREES, color=BLUE_B)
        AS8 = AnnularSector(inner_radius=3.3, outer_radius=3.5, angle=angle_length * DEGREES,
                            start_angle=start_angles[8] * DEGREES, color=GREEN_E)
        AS9 = AnnularSector(inner_radius=3.3, outer_radius=3.5, angle=angle_length * DEGREES,
                            start_angle=start_angles[9] * DEGREES, color=GREEN_B)

        # 最外框每一段环形添加到场景中
        self.add(AS0, AS1, AS2, AS3, AS4, AS5, AS6, AS7, AS8, AS9)
        self.wait(0.5)

        # 圆周率小数点后10000位
        TotalNum = 10000.0
        # 圆周率小数点前的那个3开始
        old_num = 3
        # 每一条贝塞尔曲线起始点和终点移动一点点，变化量初始值如下
        angle_dy = angle_length / TotalNum
        # 每一条贝塞尔曲线减淡一点点，变化量初始值如下
        alpha_dy = 0.2
        bezier_b = 1
        i = 0
        # 曲线实际开始的位置与最外框隔开一点距离
        end_r = 3.2

        # 开始读取小数点后10000位的存储文件
        with open('pi.txt') as file_read:
            while True:
                c = file_read.read(1)
                i += 1
                if not c:
                    print("End of file")
                    break
                if i > TotalNum:
                    break

                # 从上次的数字，准备画曲线到文件里读到的新的一个数字
                # 计算起始点和终点的角度
                start_pos_angle = math.radians(start_angles[old_num] + angle_length - angle_dy)
                end_pos_angle = math.radians(start_angles[int(c)] + angle_length - angle_dy)

                # 转换成起始点和终点的坐标
                start_pos_angle_cos = math.cos(start_pos_angle)
                start_pos_angle_sin = math.sin(start_pos_angle)
                end_pos_angle_cos = math.cos(end_pos_angle)
                end_pos_angle_sin = math.sin(end_pos_angle)

                start_pos = np.array((end_r * start_pos_angle_cos, end_r * start_pos_angle_sin, 0.0))
                end_pos = np.array((end_r * end_pos_angle_cos, end_r * end_pos_angle_sin, 0.0))

                # 计算旧数字和新数字的差值，来决定曲线从圆心左边绕过去，还是从右边绕过去
                diff = int(c) - old_num

                # 如果数值相同，那么贝塞尔曲线实际是直上直下
                if (diff == 0):
                    start_pos_b = np.array((bezier_b * start_pos_angle_cos, bezier_b * start_pos_angle_sin, 0.0))
                    end_pos_b = np.array((bezier_b * end_pos_angle_cos, bezier_b * end_pos_angle_sin, 0.0))
                # 如果新数值在右手边，那么就从右边绕过去
                elif (diff >= 5 or (diff < 0 and diff >= -5)):
                    end_b_num = int(c) + 4
                    if end_b_num > 9:
                        end_b_num -= 10
                    start_b_num = old_num - 4
                    if start_b_num < 0:
                        start_b_num += 10

                    end_b_pos_angle = math.radians(start_angles[end_b_num] + angle_length - angle_dy)
                    end_b_pos_angle_cos = math.cos(end_b_pos_angle)
                    end_b_pos_angle_sin = math.sin(end_b_pos_angle)
                    end_b_pos = np.array((end_r * end_b_pos_angle_cos, end_r * end_b_pos_angle_sin, 0.0))
                    start_b_pos_angle = math.radians(start_angles[start_b_num] + angle_length - angle_dy)
                    start_b_pos_angle_cos = math.cos(start_b_pos_angle)
                    start_b_pos_angle_sin = math.sin(start_b_pos_angle)
                    start_b_pos = np.array((end_r * start_b_pos_angle_cos, end_r * start_b_pos_angle_sin, 0.0))

                    start_pos_b = (start_b_pos - start_pos) * 0.3 + start_pos
                    end_pos_b = (end_b_pos - end_pos) * 0.3 + end_pos
                # 如果新数值在左手边，那么就从左边绕过去
                else:
                    end_b_num = int(c) - 4
                    if end_b_num < 0:
                        end_b_num += 10
                    start_b_num = old_num + 4
                    if start_b_num > 9:
                        start_b_num -= 10

                    end_b_pos_angle = math.radians(start_angles[end_b_num] + angle_length - angle_dy)
                    end_b_pos_angle_cos = math.cos(end_b_pos_angle)
                    end_b_pos_angle_sin = math.sin(end_b_pos_angle)
                    end_b_pos = np.array((end_r * end_b_pos_angle_cos, end_r * end_b_pos_angle_sin, 0.0))
                    start_b_pos_angle = math.radians(start_angles[start_b_num] + angle_length - angle_dy)
                    start_b_pos_angle_cos = math.cos(start_b_pos_angle)
                    start_b_pos_angle_sin = math.sin(start_b_pos_angle)
                    start_b_pos = np.array((end_r * start_b_pos_angle_cos, end_r * start_b_pos_angle_sin, 0.0))

                    start_pos_b = (start_b_pos - start_pos) * 0.3 + start_pos
                    end_pos_b = (end_b_pos - end_pos) * 0.3 + end_pos

                # 画贝塞尔曲线
                bezier = CubicBezier(start_pos, start_pos_b, end_pos_b, end_pos, stroke_color=colors[old_num],
                                     stroke_width=0.4, stroke_opacity=alpha_dy)

                self.add(bezier)

                # 循环迭代常规处理
                old_num = int(c)
                angle_dy += (angle_length / TotalNum)
                alpha_dy -= (0.17 / TotalNum)

        # 以上圆周率圆盘就画完了

        # 以下是为了做mv加的动画效果
        # 基本上重复着再来一次，只不过少挑一些数字
        TotalNum = 30.0
        old_num = 3
        angle_dy = angle_length / TotalNum
        alpha_dy = 0.4
        bezier_b = 1
        i = 0
        end_r = 3.2

        with open('pi.txt') as file_read:
            while True:
                c = file_read.read(1)
                i += 1
                if not c:
                    print("End of file")
                    break
                if i > TotalNum:
                    break
                start_pos_angle = math.radians(start_angles[old_num] + angle_length - angle_dy)
                end_pos_angle = math.radians(start_angles[int(c)] + angle_length - angle_dy)

                start_pos_angle_cos = math.cos(start_pos_angle)
                start_pos_angle_sin = math.sin(start_pos_angle)
                end_pos_angle_cos = math.cos(end_pos_angle)
                end_pos_angle_sin = math.sin(end_pos_angle)

                start_pos = np.array((end_r * start_pos_angle_cos, end_r * start_pos_angle_sin, 0.0))
                end_pos = np.array((end_r * end_pos_angle_cos, end_r * end_pos_angle_sin, 0.0))

                diff = int(c) - old_num

                if (diff == 0):
                    start_pos_b = np.array((bezier_b * start_pos_angle_cos, bezier_b * start_pos_angle_sin, 0.0))
                    end_pos_b = np.array((bezier_b * end_pos_angle_cos, bezier_b * end_pos_angle_sin, 0.0))
                elif (diff >= 5 or (diff < 0 and diff >= -5)):
                    end_b_num = int(c) + 4
                    if end_b_num > 9:
                        end_b_num -= 10
                    start_b_num = old_num - 4
                    if start_b_num < 0:
                        start_b_num += 10

                    end_b_pos_angle = math.radians(start_angles[end_b_num] + angle_length - angle_dy)
                    end_b_pos_angle_cos = math.cos(end_b_pos_angle)
                    end_b_pos_angle_sin = math.sin(end_b_pos_angle)
                    end_b_pos = np.array((end_r * end_b_pos_angle_cos, end_r * end_b_pos_angle_sin, 0.0))
                    start_b_pos_angle = math.radians(start_angles[start_b_num] + angle_length - angle_dy)
                    start_b_pos_angle_cos = math.cos(start_b_pos_angle)
                    start_b_pos_angle_sin = math.sin(start_b_pos_angle)
                    start_b_pos = np.array((end_r * start_b_pos_angle_cos, end_r * start_b_pos_angle_sin, 0.0))

                    start_pos_b = (start_b_pos - start_pos) * 0.3 + start_pos
                    end_pos_b = (end_b_pos - end_pos) * 0.3 + end_pos
                else:
                    end_b_num = int(c) - 4
                    if end_b_num < 0:
                        end_b_num += 10
                    start_b_num = old_num + 4
                    if start_b_num > 9:
                        start_b_num -= 10

                    end_b_pos_angle = math.radians(start_angles[end_b_num] + angle_length - angle_dy)
                    end_b_pos_angle_cos = math.cos(end_b_pos_angle)
                    end_b_pos_angle_sin = math.sin(end_b_pos_angle)
                    end_b_pos = np.array((end_r * end_b_pos_angle_cos, end_r * end_b_pos_angle_sin, 0.0))
                    start_b_pos_angle = math.radians(start_angles[start_b_num] + angle_length - angle_dy)
                    start_b_pos_angle_cos = math.cos(start_b_pos_angle)
                    start_b_pos_angle_sin = math.sin(start_b_pos_angle)
                    start_b_pos = np.array((end_r * start_b_pos_angle_cos, end_r * start_b_pos_angle_sin, 0.0))

                    start_pos_b = (start_b_pos - start_pos) * 0.3 + start_pos
                    end_pos_b = (end_b_pos - end_pos) * 0.3 + end_pos
                bezier = CubicBezier(start_pos, start_pos_b, end_pos_b, end_pos, stroke_color=colors[old_num],
                                     stroke_width=0.4, stroke_opacity=alpha_dy)

                # 生成个圆点，沿着贝塞尔曲线移动，生成动画
                path = VMobject()
                path.set_stroke(color=colors[old_num], width=1.8, opacity=1.0)
                dot = Dot()
                dot.move_to(start_pos)
                path.set_points_as_corners([dot.get_center(), dot.get_center()])

                def update_path(path):
                    previous_path = path.copy()
                    previous_path.add_points_as_corners([dot.get_center()])
                    path.become(previous_path)

                path.add_updater(update_path)
                self.add(dot)
                self.add(path)
                self.play(MoveAlongPath(dot, bezier), run_time=2, rate_func=smooth)
                # path.remove_updater(update_path)
                self.play(FadeOut(dot, path))
                self.wait(0.1)

                old_num = int(c)
                angle_dy += (angle_length / TotalNum)
                alpha_dy -= (0.3 / TotalNum)

        self.wait(1)

"""把这个文件在imports里导入就可以用了"""
import sys 
sys.path.append(r"D:\Program Files\manim-master")
from manimlib.imports import *

"""这两个类的相类似，
不过第一个类是通过比率确定向量的各项长度参数，如底面半径，箭头的长度
第二个类是直接给定向量的各项长度参数"""
class ThreeDVector(VMobject):
    """
    这个类的原理是：
    向量主体和向量顶端都是圆锥，
    两个圆锥的底面圆都是用多边形近似的圆，
    两个圆锥的侧面也都是用多边形拼接的，
    所以delta_theta是控制多边形近似圆的精度的(越小精度越高)
    """
    CONFIG = {
    "ratio_of_tip_length_to_vector_length":1/7,#顶端圆锥长度与向量长度的比
    "ratio_of_tbr_to_br":1.5,#顶端圆锥的底面半径与向量主体的底面半径之比

    "max_bottom_radius":0.1,#向量主体底面圆的最大半径
    "max_tip_length":0.4,#顶端圆锥最大长度(圆锥的高)

    "bottom_circle_side_color":None,#向量主体的底面圆的边框颜色这个颜色也可以自己在源代码改一下，改成BLACK或其它颜色
    "tip_bottom_circle_side_color":None,#顶端圆锥的底面圆的边框颜色，这个同上可以改一下

    "bottom_circle_delta_theta":0.4,#向量主体底面圆的delta_theta
    "tip_bottom_circle_delta_theta":0.4,#顶端圆锥底面圆的delta_theta

    "bottom_circle_side_width":2,#向量主体圆锥的底面圆的边框大小
    "tip_bottom_circle_side_width":2,#顶端圆锥的底面圆的边框的大小

    "fill_opacity":0.8,
    }

    def __init__(self,direction=RIGHT,**kwargs):
        VMobject.__init__(self,**kwargs)
        self.direction = np.array(direction,dtype=np.float)
        self.l = get_norm(self.direction)
        if self.l != 0:
            self.get_and_reset_some_parameters()
            self.get_rotation_matrix()
            self.get_bottom_circle_points()
            self.get_tip_circle_points()
            self.get_cone()
            self.get_tip_cone()
            self.add(
                self.bottom_circle,
                self.tip_bottom_circle,
                self.cone_side,
                self.tip_cone_side
                )

    def get_and_reset_some_parameters(self):
        tl = self.l*self.ratio_of_tip_length_to_vector_length
        if tl >= self.max_tip_length :#确定顶端圆锥的高度
            self.tip_length = self.max_tip_length
        else:
            self.tip_length = tl
        #第47行(下一行)确定了顶端圆锥高度与顶端圆锥底面半径的关系，即顶端圆锥底面半径等于顶端圆锥高度的一半，可自己更改
        self.tip_bottom_radius = self.tip_length/2
        br = self.tip_bottom_radius/self.ratio_of_tbr_to_br
        if br > self.max_bottom_radius:#确定了向量主体的底面半径
            self.bottom_radius = self.max_bottom_radius
        else:
            self.bottom_radius = br
        
        self.original_direction = self.direction.copy()
        self.tcotbc = self.direction*(self.l-self.tip_length)/self.l#the center of tip bottom circle 底端圆锥的底面圆的圆心位置
        a_ratio = 1.05#一般0到1,你也可以尝试一下负数(比如-2)或大于1的数(比如2)，看看会发生什么
        self.direction *= (self.l-a_ratio*self.tip_length)/self.l#将direction重置成向量主体圆锥的顶点的坐标

        if self.bottom_circle_side_color == None:
            self.bottom_circle_side_color = self.color
        if self.tip_bottom_circle_side_color == None:
            self.tip_bottom_circle_side_color = self.color

    def get_rotation_matrix(self):
        rho = get_norm(self.direction[:2])
        r = get_norm(self.direction)
        cos_phi = self.direction[2] / r
        sin_phi = rho / r

        if rho != 0:
            cos_theta = self.direction[0] / rho
            sin_theta = self.direction[1] / rho
        else:
            cos_theta = 1
            sin_theta = 0

        M_z = np.array([
            [cos_theta,-sin_theta,0],
            [sin_theta,cos_theta,0],
            [0,0,1]
            ])

        M_y = np.array([
            [cos_phi,0,sin_phi],
            [0,1,0],
            [-sin_phi,0,cos_phi]
            ])

        self.rotation_matrix = np.dot(M_z,M_y)

    def get_bottom_circle_points(self):
        thetas = np.arange(0,2*np.pi+self.bottom_circle_delta_theta,self.bottom_circle_delta_theta,dtype=np.float64)
        points = np.vstack((
            self.bottom_radius*np.cos(thetas),
            self.bottom_radius*np.sin(thetas),
            np.zeros_like(thetas)))
        self.bc_points = list(np.dot(self.rotation_matrix,points).T)

    def get_tip_circle_points(self):
        thetas = np.arange(0,2*np.pi+self.tip_bottom_circle_delta_theta,self.tip_bottom_circle_delta_theta)
        points = np.vstack((
            self.tip_bottom_radius*np.cos(thetas),
            self.tip_bottom_radius*np.sin(thetas),
            np.zeros_like(thetas)))
        self.tbc_points = list(np.dot(self.rotation_matrix,points).T + self.tcotbc)

    def get_cone(self):
        self.bottom_circle = Polygon(
            *self.bc_points,
            color=self.color,#向量主体圆锥的底面圆的颜色，可自己修改
            fill_opacity=self.fill_opacity,
            stroke_width=self.bottom_circle_side_width,
            stroke_color=self.bottom_circle_side_color)

        self.cone_side = VGroup()

        for i in range(len(self.bc_points) - 1):
            self.cone_side.add(Polygon(
                *[*self.bc_points[i:i+2],self.direction],
                color=self.color,#向量主体圆锥的侧面的颜色
                fill_opacity=self.fill_opacity,#
                stroke_width=0,#用来拼接侧面的多边形的边框的大小
                stroke_color=self.color)#用来拼接侧面的多边形的边框的颜色
            )

    def get_tip_cone(self):
        self.tip_bottom_circle = Polygon(
            *self.tbc_points,
            color=self.color,#顶端圆锥的底面圆的颜色
            fill_opacity=self.fill_opacity,
            stroke_width=self.tip_bottom_circle_side_width,
            stroke_color=self.tip_bottom_circle_side_color)

        self.tip_cone_side = VGroup()
        for i in range(len(self.bc_points) - 1):
            self.cone_side.add(Polygon(
                *[*self.tbc_points[i:i+2],self.original_direction],
                color=self.color,#顶端圆锥的侧面的颜色
                fill_opacity=self.fill_opacity,#
                stroke_width=0,#用来拼接侧面的多边形的边框的大小
                stroke_color=self.color)#用来拼接侧面的多边形的边框的颜色
            )

class ThreeDVector2(VMobject):
    """
    这个类的原理是：
    向量主体和向量顶端都是圆锥，
    两个圆锥的底面圆都是用多边形近似的圆，
    两个圆锥的侧面也都是用多边形拼接的，
    所以delta_theta是控制多边形近似圆的精度的(越小精度越高)
    """
    CONFIG = {
    "bottom_radius":0.1,#向量主体的底面圆半径
    "tip_bottom_radius":0.2,#顶端圆锥的底面半径,建议是bottom_radius的四倍
    "tip_length":0.4,#顶端圆锥的长(圆锥的高)，建议是tip_bottom_radius的两倍

    "bottom_circle_side_color":None,#向量主体的底面圆的边框颜色这个颜色也可以自己在源代码改一下，改成BLACK或其它颜色
    "tip_bottom_circle_side_color":None,#顶端圆锥的底面圆的边框颜色，这个同上可以改一下

    "bottom_circle_delta_theta":0.4,#向量主体底面圆的delta_theta
    "tip_bottom_circle_delta_theta":0.4,#顶端圆锥底面圆的delta_theta

    "bottom_circle_side_width":2,#向量主体圆锥的底面圆的边框大小
    "tip_bottom_circle_side_width":2,#顶端圆锥的底面圆的边框的大小

    "fill_opacity":0.8,
    }

    def __init__(self,direction=RIGHT,**kwargs):
        VMobject.__init__(self,**kwargs)
        self.direction = np.array(direction,dtype=np.float)
        self.l = get_norm(self.direction)
        if self.l != 0:
            self.get_and_reset_some_parameters()
            self.get_rotation_matrix()
            self.get_bottom_circle_points()
            self.get_tip_circle_points()
            self.get_cone()
            self.get_tip_cone()
            self.add(
                self.bottom_circle,
                self.tip_bottom_circle,
                self.cone_side,
                self.tip_cone_side
                )

    def get_and_reset_some_parameters(self):
        self.original_direction = self.direction.copy()
        self.tcotbc = self.direction*(self.l-self.tip_length)/self.l#the center of tip bottom circle 底端圆锥的底面圆的圆心位置
        a_ratio = 1.05#一般0到1,你也可以尝试一下负数(比如-2)或大于1的数(比如2)，看看会发生什么
        self.direction *= (self.l-a_ratio*self.tip_length)/self.l#将direction重置成向量主体圆锥的顶点的坐标

        if self.bottom_circle_side_color == None:
            self.bottom_circle_side_color = self.color
        if self.tip_bottom_circle_side_color == None:
            self.tip_bottom_circle_side_color = self.color

    def get_rotation_matrix(self):
        rho = get_norm(self.direction[:2])
        r = get_norm(self.direction)
        cos_phi = self.direction[2] / r
        sin_phi = rho / r

        if rho != 0:
            cos_theta = self.direction[0] / rho
            sin_theta = self.direction[1] / rho
        else:
            cos_theta = 1
            sin_theta = 0

        M_z = np.array([
            [cos_theta,-sin_theta,0],
            [sin_theta,cos_theta,0],
            [0,0,1]
            ])

        M_y = np.array([
            [cos_phi,0,sin_phi],
            [0,1,0],
            [-sin_phi,0,cos_phi]
            ])

        self.rotation_matrix = np.dot(M_z,M_y)

    def get_bottom_circle_points(self):
        thetas = np.arange(0,2*np.pi+self.bottom_circle_delta_theta,self.bottom_circle_delta_theta,dtype=np.float64)
        points = np.vstack((
            self.bottom_radius*np.cos(thetas),
            self.bottom_radius*np.sin(thetas),
            np.zeros_like(thetas)))
        self.bc_points = list(np.dot(self.rotation_matrix,points).T)

    def get_tip_circle_points(self):
        thetas = np.arange(0,2*np.pi+self.tip_bottom_circle_delta_theta,self.tip_bottom_circle_delta_theta)
        points = np.vstack((
            self.tip_bottom_radius*np.cos(thetas),
            self.tip_bottom_radius*np.sin(thetas),
            np.zeros_like(thetas)))
        self.tbc_points = list(np.dot(self.rotation_matrix,points).T + self.tcotbc)

    def get_cone(self):
        self.bottom_circle = Polygon(
            *self.bc_points,
            color=self.color,#向量主体圆锥的底面圆的颜色，可自己修改
            fill_opacity=self.fill_opacity,
            stroke_width=self.bottom_circle_side_width,
            stroke_color=self.bottom_circle_side_color)

        self.cone_side = VGroup()

        for i in range(len(self.bc_points) - 1):
            self.cone_side.add(Polygon(
                *[*self.bc_points[i:i+2],self.direction],
                color=self.color,#向量主体圆锥的侧面的颜色
                fill_opacity=self.fill_opacity,
                stroke_width=0,#用来拼接侧面的多边形的边框的大小
                stroke_color=self.color)#用来拼接侧面的多边形的边框的颜色
            )

    def get_tip_cone(self):
        self.tip_bottom_circle = Polygon(
            *self.tbc_points,
            color=self.color,#顶端圆锥的底面圆的颜色
            fill_opacity=self.fill_opacity,
            stroke_width=self.tip_bottom_circle_side_width,
            stroke_color=self.tip_bottom_circle_side_color)

        self.tip_cone_side = VGroup()
        for i in range(len(self.bc_points) - 1):
            self.cone_side.add(Polygon(
                *[*self.tbc_points[i:i+2],self.original_direction],
                color=self.color,#顶端圆锥的侧面的颜色
                fill_opacity=self.fill_opacity,
                stroke_width=0,#用来拼接侧面的多边形的边框的大小
                stroke_color=self.color)#用来拼接侧面的多边形的边框的颜色
            )

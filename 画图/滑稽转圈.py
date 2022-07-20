import turtle as t
import random


t.register_shape('huaji.gif')
t.shape('huaji.gif')


t.speed(0)
t.pensize(1)
t.pencolor('red')
angle = 1
while 1:
    t.fd(angle)
    t.left(angle)

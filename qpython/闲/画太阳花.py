import turtle as t
import time
t.color("red", "yellow")
t.speed(0)
t.begin_fill()
for _ in range(50):
    t.forward(200)
    t.left(170)
t.end_fill()
t.pu()
t.goto(-150,-150)
t.pd()
t.write("hello")
time.sleep(3)
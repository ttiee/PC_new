import turtle as t
# import time


# t.speed(0)


def yuan(angle):
    t.pu()
    t.goto(0, 0)
    t.seth(angle)
    t.forward(200)
    t.pd()
    t.fillcolor('black')
    t.begin_fill()
    t.left(90)
    t.circle(200, 180)
    t.end_fill()

    t.fillcolor('white')
    t.begin_fill()
    t.circle(200, 180)
    t.end_fill()

    t.fillcolor('white')
    t.begin_fill()
    t.circle(100, 180)
    t.end_fill()

    t.fillcolor('black')
    t.begin_fill()
    t.circle(-100, 180)
    t.end_fill()

    t.right(90)
    t.pu()
    t.forward(100)
    t.pd()
    t.dot(60, 'white')
    t.pu()
    t.forward(200)
    t.pd()
    t.dot(60, 'black')


ang = 0
t.hideturtle()
while True:
    t.clear()
    t.tracer(0, 0)
    ang += 1
    yuan(angle=ang)
    t.tracer(10, 10)
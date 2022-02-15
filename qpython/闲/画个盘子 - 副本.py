import turtle as a
a.colormode(1)


def b():
	c=["red","orange","yellow","gold","purple"]
	a.pu()
	a.fd(-80)
	a.pd()
	a.left(9)
	a.pensize(1)
	a.speed(1000)
	for i in range(20):
		a.pencolor(c[i%5])
		a.fd(140)
		a.left(162)
	a.fd(70)


for i in range(40):
	b()
a.hideturtle()
a.done()

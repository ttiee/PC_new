import turtle as a
a.speed(0)
a.pu()
a.fd(70)
a.pd()
c=["red","yellow","green","blue"]
a.pensize(10)
for i in range(200):
	a.left(91)
	a.pencolor(c[i%4])
	a.fd(i+70)
for b in range(200):
	a.pencolor(c[b%4])
	a.left(91)
	a.fd(270)
a.left(45)
for d in range(4):
	a.pensize(20)
	a.pencolor(c[d%4])
	f=135*2**(1/2)
	a.circle(f,90)
a.hideturtle()
a.done()
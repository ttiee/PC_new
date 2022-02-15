import pygame as p
sceen=p.display.set_mode((140,140))
sceen.fill((255,255,255))
p.display.update()
a=p.image.load('song1.png')
b=p.image.load('bir1.png')
sceen.blit(a,(20,20))
sceen.blit(b,(-8,-18))
c=sceen
c=p.transform.scale(c,(7000,11000))
sceen.blit(c,(0,0))
p.display.update()
p.image.save(sceen,'pirthday1.png',)
while True:
	pass
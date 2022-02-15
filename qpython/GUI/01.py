import time as t
from tkinter import *
from tkinter import messagebox
#import game2


root = Tk()

root.title('hhh')
root.geometry('500x300+100+100')

def main():
	print('hh')


def a(e):
	for i in range(1):
		messagebox.showinfo("hello","give me a kiss")
	messagebox.showinfo("hi","I am Kitty")
	
def b(e):
	messagebox.showinfo('人生重开模拟器','Game Over')
	main()
	



btn01 = Button(root)
btn01["text"] = "click"
btn01.pack()

btn01.bind("<Button-1>",a)


btn02 = Button(root)
btn02['text'] = '人生重开模拟器'
btn02.pack()

btn02.bind('<Button-1>',b)




root.mainloop()

t.sleep(1)

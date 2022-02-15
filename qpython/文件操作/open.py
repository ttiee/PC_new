import os


print(os.getcwd())

os.chdir("/storage/emulated/0/qpython/文件操作/")
print(os.getcwd())

with open("a.dat","ab") as f:
    f.write("你好a".encode("utf-8"))


try:
  	f = open("all.txt","a")
  	s = str("呀养鬼为祸")
  	f.write(s)
finally:
  	f.close()
  	
  	
with open("../图片/2.png","rb") as f:
    png = f.read()


#for i in range(2):

with open("3.png","wb") as f:
    f.write(png)
print(os.path.getsize("3.png"))



print(os.listdir(os.getcwd()))  	
  	
  	
  	
  	
  	
  	
  	
  	
  	

  	
  	
  	

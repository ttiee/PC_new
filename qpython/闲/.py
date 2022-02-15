try:
  	f = open("all.txt","a")
  	s = str("结果1 if 表达式 else 结果2".encode("GBK").decode("UTF-8","replace"))
  	f.write(s)
finally:
   	f.close()
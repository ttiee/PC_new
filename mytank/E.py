with open('按键.jpg', 'br') as f:
    a = f.read()

with open('坦克大战全部图片.zip', 'br') as f:
    b = f.read()
with open('坦克大战全部图片.jpg', 'bw') as f:
    f.write(a)
    f.write(b)


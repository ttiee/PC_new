with open('open.mp3', 'br') as f:
    a = f.read()

with open('open1.jpg', 'bw') as f:
    f.write(a)


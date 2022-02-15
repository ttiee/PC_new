with open('open.jpg', 'br') as f:
    a = f.read()

with open('open.mp3', 'bw') as f:
    f.write(a)

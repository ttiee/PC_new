import turtle as t


print(t.getshapes())
# ['arrow', 'blank', 'circle', 'classic', 'square', 'triangle', 'turtle']
t.shape(name='turtle')
# help(t.register_shape)
t.register_shape('huaji.gif')
print(t.getshapes())
t.shape('huaji.gif')
for i in range(10):
    t.goto(100, 100)
    t.goto(0, 0)
t.goto(100, 100)
t.done()
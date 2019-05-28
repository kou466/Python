import turtle as t

default_shape = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']
user_shape = ['7s0.gif', '7s1.gif', '7s2.gif']

for i in default_shape:
    t.shape(i)
    t.delay(1000)
for j in user_shape:
    t.addshape(j)
    t.shape(j)
    t.delay(1000)
t.mainloop()

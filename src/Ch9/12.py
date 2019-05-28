import turtle as t

t.setup(300, 300)
s = t.Screen()
t.shape('turtle')
t.clear()
t.home()


def draw():
    t.pendown()
    t.fd(10)
    t.penup()


def turn_left():
    t.setheading(180)
    draw()


def turn_right():
    t.setheading(0)
    draw()


def turn_forward():
    t.setheading(90)
    draw()


def turn_backward():
    t.setheading(270)
    draw()


s.onkey(turn_forward, "Up")
s.onkey(turn_backward, "Down")
s.onkey(turn_left, "Left")
s.onkey(turn_right, "Right")
s.onkey(t.reset, "r")
s.listen()
t.mainloop()

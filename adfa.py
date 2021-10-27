import turtle as trtl
t = trtl.Turtle()

m = int(input("What is the slope of the line? -> "))
b = int(input("What is the y-intercept? -> "))


sx = 1
sy = m - b
t.penup()
t.setposition(0, b)
t.setposition(sx, sy)

wn = trtl.Screen()
wn.mainloop()
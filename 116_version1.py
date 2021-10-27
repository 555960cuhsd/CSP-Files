#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()
painter.pensize(40)
painter.circle(20)
legs = 6
length = 70
direction = 380 / legs
painter.pensize(5)
count = 0
while (count < legs):
  painter.goto(0,0)
  painter.setheading(direction*count)
  painter.forward(length)
  count = count + 1
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()
# Create a spider body
painter.pensize(40)
painter.circle(20)

# Configure spider legs
legs = 8
length = 70
direction = 360 / legs

# Draw legs
painter.pensize(5)
count = 0
while (count < legs):
  painter.goto(0,20)
  painter.setheading(direction*count)
  painter.forward(length)
  count = count + 1
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
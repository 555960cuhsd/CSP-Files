#   a116_buggy_image.py
import turtle as trtl
# instead of a descriptive name of the turtle such as painter,
# a less useful variable name x is used
painter = trtl.Turtle()
# Create a spider body
painter.pensize(40)
painter.circle(20)

# Spider eyes
painter.penup()
painter.goto(-35, 15)
painter.left(45)
painter.pensize(2)
painter.color("white")
for i in range(2):
  painter.forward(20)
  painter.pendown()
  painter.begin_fill()
  painter.circle(3)
  painter.end_fill()
  painter.penup()

# Configure spider legs
legs = 8
length = 70
direction = 360 / legs

# Draw legs
painter.color("black")
painter.pensize(5)
count = 0
while (count < legs):
  painter.goto(0,20)
  painter.pendown()
  if count < 4:
    painter.setheading(direction*count - count * 22.5)
  elif count >= 4:
    painter.setheading(direction*count + 90 - count * 22.5)
  painter.forward(length)
  count = count + 1
painter.hideturtle()
wn = trtl.Screen()
wn.mainloop()
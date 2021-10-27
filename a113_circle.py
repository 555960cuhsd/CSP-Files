#   a113_circle_of_circles.py
#   Modify this code to draw a circle of cirlces
import turtle as trtl

painter = trtl.Turtle()
painter.shape("circle")
for i in range(18):
  painter.forward(20)
  painter.right(20)
  painter.stamp()
wn = trtl.Screen()
wn.mainloop()
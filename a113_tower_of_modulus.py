#   a113_tower.py
#   Modify this code in VS Code to alternate the colors of the 
#   floors every three floors
import turtle as trtl

painter = trtl.Turtle()
painter.speed(0)
painter.pensize(5)

# starting location of the tower
x = -300
y = -150

# height of tower and a counter for each floor
num_floors = 63
floor = 0

# iterate
while floor < num_floors:
  # set placement and color of turtle
  painter.penup()
  if floor % 21 == 0: # making a new building every 21 floors
    x = x + 150
    y = -150
  painter.goto(x, y)

  # setting the turtle's colors
  if floor % 9 <= 2:
   painter.color("red")
  if floor % 9 >= 3 <= 5:
    painter.color("blue")
  if floor % 9 >= 6:
    painter.color("purple")

  y = y + 5 # location of next floor
  floor = floor + 1
  

  #draw the floor
  painter.pendown()
  painter.forward(50)

wn = trtl.Screen()
wn.mainloop()
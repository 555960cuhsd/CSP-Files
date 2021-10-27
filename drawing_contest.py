'''
THIS WORK IS MADE BY *JAY UM* AND *JUSTIN LEE*

This project makes the Earth with the Sun in the background, stars are created all around and are randomized.
'''

import turtle as trtl
import random
t = trtl.Turtle()
t.speed(0)
def move(a, b):
  t.penup()
  t.setpos(a, b)
  t.pendown()

# Making the black background
t.begin_fill()
move(-1000,-1000)
t.pencolor("black")
for i in range(4):
  t.forward(2000)
  t.left(90)
t.end_fill()

# Defining a star
def star():
  t.forward(8)
  t.backward(4)
  t.left(90)
  t.forward(4)
  t.backward(8)

# Making the randomized stars
t.pencolor("white")
t.pensize(3)
for i in range(100):
  move(random.randrange(-400, 401), random.randrange(-400, 401))
  star()

# Making the Earth
t.pensize(1)
move(-250, -500)
t.color("#6495ED")
t.begin_fill()
t.circle(250)
t.end_fill()

# Creating the land on the Earth
move(-220, -400)
t.color("#00cf00")
t.begin_fill()
t.circle(120)
t.end_fill()

move(-170, -270)
t.begin_fill()
t.circle(80)
t.end_fill()

move(-300, -120)
t.begin_fill()
t.circle(30)
t.end_fill()

# Making the Sun

t.setheading(0)
t.color("#ffc629")
move(200,180)
t.begin_fill()
t.circle(20)
t.end_fill()
move(200, 200)
t.left(10)
for i in range(8):
  t.forward(30)
  t.backward(30)
  t.left(45)

wn = trtl.Screen()
wn.mainloop()
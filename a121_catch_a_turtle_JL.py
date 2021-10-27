# a121_catch_a_turtle.py
#-----import statements-----
import turtle as trtl
import random as rand

#-----initialize turtle-----
isosceles_triangle = trtl.Turtle()
isosceles_triangle.speed(0)
isosceles_triangle_color = "blue"
isosceles_triangle_shape = "triangle"
isosceles_triangle.penup()

# Score box
score_writer = trtl.Turtle()

score_writer.speed(0)
score_writer.penup()
score_writer.setposition(-180, 180)
score_writer.pendown()
score_writer.write("Score")
score_writer.penup()
score_writer.setposition(-200, 200)
score_writer.pendown()
for i in range(2):
  score_writer.forward(70)
  score_writer.left(90)
  score_writer.forward(20)
  score_writer.left(90)
score_writer.penup()
score_writer.setposition(-165, 210)
score_writer.pendown()
score_writer.circle(1)
score_writer.hideturtle()

# Countdown timer
score_writer.penup()
score_writer.setposition(145, 180)
score_writer.pendown()
score_writer.write("Timer")
score_writer.penup()
score_writer.setposition(200, 200)
score_writer.pendown()
for i in range(2):
  score_writer.backward(90)
  score_writer.right(90)
  score_writer.backward(20)
  score_writer.right(90)
score_writer.penup()
score_writer.setposition(155, 210)
score_writer.pendown()
score_writer.circle(1)
score_writer.hideturtle()


#-----game configuration----
isosceles_triangle.shape(isosceles_triangle_shape)
isosceles_triangle.shapesize(1, 3, 0)
isosceles_triangle.fillcolor(isosceles_triangle_color)
score = 0

#-----game functions--------
def isosceles_triangle_clicked(x, y):
  update_score()
  change_position()

def change_position():
  new_xpos = rand.randint(-200, 200)
  new_ypos = rand.randint(-150, 150)
  isosceles_triangle.hideturtle()
  isosceles_triangle.setposition(new_xpos, new_ypos)
  isosceles_triangle.showturtle()

def update_score():
  global score
  score += 1
  print(score)

#-----events----------------
isosceles_triangle.onclick(isosceles_triangle_clicked)

wn = trtl.Screen()
wn.mainloop()
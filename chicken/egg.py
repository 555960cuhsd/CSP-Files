import random as rand
import turtle as trtl

### Game setup ###
wn = trtl.Screen()
wn.addshape("chicken.gif")

# Score Writer
score_writer = trtl.Turtle()
score_writer.penup()
score_writer.hideturtle()
score_writer.setposition(-200, -200)
score_writer.pendown()

score_rate = 1

# Chicken
egg = trtl.Turtle()
score = 0
egg.shape("chicken.gif")
egg.speed(0)
egg.penup()

font_setup = ("Arial", "15", "normal")

# Point Text
p = trtl.Turtle()
p.hideturtle()
p.speed(3)

# Upgrade Button
button = trtl.Turtle()


### Game functions ###

def eg_click(x, y):
  update_score()
  change_position()
  point()

def change_position():
  new_xpos = rand.randint(-200, 200)
  new_ypos = rand.randint(-150, 150)
  egg.hideturtle()
  egg.setposition(new_xpos, new_ypos)
  egg.showturtle()

def update_score():
  score_writer.clear()
  global score
  score += 1
  print(score)
  score_writer.write(str(score) + " eggs!", font = font_setup)


def point():
  p.penup()
  p.setposition(egg.xcor(), egg.ycor())
  p.pendown()
  p.write("+"+str(score_rate))
  p.clear()
  



egg.onclick(eg_click)

wn.mainloop()


import turtle as t
import random
tim = t.Turtle()

########### Challenge 3 - Draw Shapes ########

screen = t.Screen()

# Setting the screen color-mode
screen.colormode(255)

for num_sides in range(3, 11):

  angle = 360 / num_sides
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255) 
  # print(b)
  tim.pencolor(r, g, b)
  
  for _ in range(num_sides):
    tim.forward(100)
    tim.right(angle)

  for _ in range(num_sides):
    tim.forward(100)
    tim.left(angle)
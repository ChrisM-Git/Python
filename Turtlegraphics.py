
import turtle
import turtle as t

turtle.colormode(255)

timmy = t.Turtle()
timmy.color("green")
timmy.shape("turtle")
import random

""" draw different shapes 
colors = ["red", "green", "blue"]
def sides(num):
  angle = 360 / num
  for _ in range(num):
    timmy.forward(100)
    timmy.right(angle)
    timmy.pencolor(random.choice(colors))


for shapeside in range(3,11):
  sides(shapeside)
"""
"""move turtle in random directions

def randomcolor():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0, 255)
  randomcolortuple = (r,g,b)
  return randomcolortuple


timmy.speed("slow")
def line(num):
  turtledirection = [0,90,180,270] # 0 is north, 90 is eest, 180 west, 270 south
  timmy.pensize(10)
  for _ in range(200):
    timmy.color
    timmy.color(randomcolor())
    timmy.forward(60)
    timmy.setheading(random.choice(turtledirection))


for num in range(0,100):
  line(num)
"""


"""Create a Spirogrpah using Turtle" with random colors"""

def randomcolor():
  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0, 255)
  randomcolortuple = (r, g, b)
  return randomcolortuple

timmy.speed("fastest")
def circle():
  timmy.color(randomcolor())
  timmy.circle(100)
  timmy.setheading(timmy.heading() + 50)

sizeofgap = 5
"""The range function doesnt like floats, which is the output type when we divide in python, need to add the int
option with range to convert the number to an int, not a float when doing division"""
for num in range(int(360 / sizeofgap)):
  circle()







"""keep at bottom of code after we modify turtle settings"""
timmyscreen = turtle.Screen()
timmyclick = turtle.exitonclick()


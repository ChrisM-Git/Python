from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=500)
screen.listen()
turtlecolor = ["blue","green","yellow","orange","red","brown"]
bet = screen.textinput(title="The Magnificant Turtle Race!", prompt="Choose your turtle color:\n blue,"
                                                                    "green,yellow,orange,red,brown")
turtle_yinpuy = [-80,-60,-40,-20,0,20]
allturtles = []

for turtles in range(0,5):
  newturtle = Turtle(shape="turtle")
  newturtle.color(turtlecolor[turtles])
  newturtle.penup()
  newturtle.goto(x=-200,y=turtle_yinpuy[turtles])
  allturtles.append(newturtle)

if bet:
  racenotfinished = True

while racenotfinished:
  for turtle in allturtles:
    if turtle.xcor() >= 250:
      racenotfinished = False
      wincolor=turtle.pencolor()
      if wincolor == bet:
        print("Your Turtle won!")
      else:
        print(f"The {wincolor} turtle won!")


      racenotfinished = False
    fwd = random.randint(0,10)
    turtle.forward(fwd)





screen.exitonclick()


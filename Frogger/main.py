import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
screen = Screen()

screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Basic Frogger")
screen.tracer(0)

player1 = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player1.Up, "Up")
screen.onkey(player1.Left, "Left")
screen.onkey(player1.Right, "Right")
screen.onkey(player1.Down, "Down")


gameon = True
while gameon:
    time.sleep(0.1)
    screen.update()
    player1
    cars.newcar()
    cars.movecar()
    for car in cars.allcars:
      if car.distance(player1) < 25:
          gameon = False
          scoreboard.gameover()




    if player1.finish():
        player1.gotostart()
        cars.levelup()
        scoreboard




screen.exitonclick()

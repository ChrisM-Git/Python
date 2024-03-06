from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.allcars = []
        self.carspeed = MOVE_INCREMENT

    def newcar(self):
        randomnum = random.randint(1,6)
        if randomnum == 1:
            newcar = Turtle("square")
            newcar.color(random.choice(COLORS))
            newcar.shapesize(stretch_wid=1, stretch_len=2)
            newcar.penup()
            random_y=random.randint(-280,280)
            newcar.goto(300,random_y)
            self.allcars.append(newcar)

    def movecar(self):
        for car in self.allcars:
            car.backward(self.carspeed)

    def levelup(self):
        self.carspeed += MOVE_INCREMENT

    def collision(self):
        for car in self.allcars:
            if car.xcor(distance=20):
                return True





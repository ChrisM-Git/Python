from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.color("blue")
        self.speed("fastest")
        self.refresh()



    def refresh(self):
        randomx = random.randint(-270, 270)
        randomy = random.randint(-270, 270)
        self.goto(randomx, randomy)




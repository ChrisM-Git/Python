from turtle import Turtle
import random
STARTPOS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
COLOR = ["orange", "red"]
#create constants so snake cant go back on itself, iei 90 to 270 thrn 90 again
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180


class Snake():
    def __init__(self):
        self.formsnake = []
        self.createsnake()
        self.head = self.formsnake[0]

    def createsnake(self):

        for segnum in STARTPOS:
            self.addsegment(segnum)

    def addsegment(self,segnum):
        newsnake = Turtle("square")
        newsnake.color("white")
        newsnake.penup()
        newsnake.goto(segnum)
        self.formsnake.append(newsnake)

    # extend the snake when it eats food
    def extend(self):
        self.addsegment(self.formsnake[-1].position())





    def move(self):

        for segnum in range(len(self.formsnake) - 1, 0, -1):
            new_x = self.formsnake[segnum - 1].xcor()
            new_y = self.formsnake[segnum - 1].ycor()
            self.formsnake[segnum].goto(new_x, new_y)

        self.formsnake[0].forward(DISTANCE)

    def Up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def Down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def Right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def Left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)







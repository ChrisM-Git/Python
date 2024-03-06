from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 380
LIVES = 3

UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.gotostart()

    def Up(self):
        if self.heading != DOWN:
            self.setheading(UP)
            self.forward(MOVE_DISTANCE)

    def Down(self):
        if self.heading != UP:
            self.setheading(DOWN)
            self.forward(MOVE_DISTANCE)

    def Left(self):
        if self.heading != RIGHT:
            self.setheading(LEFT)
            self.forward(MOVE_DISTANCE)

    def Right(self):
        if self.heading != LEFT:
            self.setheading(RIGHT)
            self.forward(MOVE_DISTANCE)

    def finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
    def reset(self):
        self.goto(STARTING_POSITION)

    def gotostart(self):
        self.goto(STARTING_POSITION)

    def died(self):
        LIVES -= 1



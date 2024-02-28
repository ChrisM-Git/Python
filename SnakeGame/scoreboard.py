from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(x=0, y=370)
        self.color("white")
        self.updatescore()

    def updatescore(self):
        self.write(f"Score: {self.score}", align = ALIGNMENT, font = FONT)

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over!",align=ALIGNMENT, font=FONT)

    def increasescore(self):
        self.score += 1
        self.clear()
        self.updatescore()
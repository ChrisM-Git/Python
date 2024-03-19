from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.goto(x=0, y=370)
        self.color("white")
        self.updatescore()

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write("Game Over!",align=ALIGNMENT, font=FONT)

    def increasescore(self):
        self.score += 1
        self.updatescore()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        with open("data.txt",mode="w") as data:
            data.write(f"{self.highscore}")
        self.score = 0
        self.updatescore()

    def updatescore(self):
        self.clear()
        self.write(f"Score: {self.score}, High Score: {self.highscore}", align=ALIGNMENT, font=FONT)







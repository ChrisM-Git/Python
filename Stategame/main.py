import turtle
import pandas
from tkinter import *
from tkinter import messagebox

from pandas.core.computation import align
ALIGNMENT = "center"
FONT = ("Arial", 11, "bold")

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("Name the States Game")

screen.addshape(image)
turtle.shape(image)
learnstates = []


data = pandas.read_csv("50_States.csv")
statelist = data.state.to_list()
tries = 4
guessedstates = []
while len(guessedstates) < 50:
    answer = screen.textinput(title=f"Guessed States {len(guessedstates)} / 50", prompt="Enter the State, type Exit to end").title()

#list comprehension list = [new_item for item in list if test]

    learnstates = [ states for states in statelist if states not in guessedstates]
    pandas.DataFrame(learnstates).to_csv("Statestolearn.csv")


    if answer in statelist:
        guessedstates.append(answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        statedata = data[data.state == answer]
        newx = int(statedata.x)
        newy = int(statedata.y)
        t.goto(newx,newy)
        t.write(answer,font=FONT, align = ALIGNMENT)
    elif answer == "Exit":
        break














""" Code to get x,y coordinates from mouse click
def get_mouse_click_coor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
"""

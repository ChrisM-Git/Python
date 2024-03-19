import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard



screen = Screen()

screen.screensize(600,600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("The Snake Game")
SPEED = 0.1

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.Up, "Up")
screen.onkey(snake.Down, "Down")
screen.onkey(snake.Left, "Left")
screen.onkey(snake.Right, "Right")

gameon = True
while gameon:
    time.sleep(SPEED)
    screen.update()
    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increasescore()
        food.refresh()
        snake.extend()
        SPEED = SPEED - 0.001


    #detect collision with wall
    if snake.head.xcor() > 420 or snake.head.xcor() < -420 or snake.head.ycor() > 420 or snake.head.ycor() < -420:
        #scoreboard.gameover() replced with highscore addition
        scoreboard.reset()
        snake.reset()
        #gameon = False

    #detect collision with tail
    for segment in snake.formsnake[1:]:
       if segment == snake.head:
          pass
       elif snake.head.distance(segment) < 4:
            #gameon = False
            scoreboard.reset()
            snake.reset()

            #scoreboard.gameover() replaced with high score addition



screen.exitonclick()

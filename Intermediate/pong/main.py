from turtle import Screen
from paddle import Paddle
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
game_on = True


paddle = Paddle()

#Paddle Controls:
screen.listen()
screen.onkeypress(paddle.go_up, "Up")
screen.onkeypress(paddle.go_down, "Down")

#Main code
while game_on:
    screen.update()
    time.sleep(0.1)












screen.exitonclick()
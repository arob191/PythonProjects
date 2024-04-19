from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Screen Initialization
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)
game_on = True

#Constants
LEFT_PADDLE = (-350, 0)
RIGHT_PADDLE = (350, 0)

#Objects
rpaddle = Paddle(RIGHT_PADDLE)
lpaddle = Paddle(LEFT_PADDLE)
ball = Ball()
l_scoreboard = Scoreboard("left")
r_scoreboard = Scoreboard("right")

#Right and Left Paddle Controls:
screen.listen()
screen.onkey(rpaddle.go_up, "Up")
screen.onkey(rpaddle.go_down, "Down")
screen.onkey(lpaddle.go_up, "w")
screen.onkey(lpaddle.go_down, "s")


#Main code
while game_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    l_scoreboard.update_score()
    r_scoreboard.update_score()

    #Detect Collision with Paddle


    #Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()











screen.exitonclick()
from turtle import Screen
from paddle import Paddle
from ball import Ball
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

    #Detect Collision with Paddle

    #Detect Collision with Wall

    #Detect When Player Scores












screen.exitonclick()
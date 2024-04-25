from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
WINNING_SCORE = 5

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
    time.sleep(ball.move_speed)
    ball.move()
    l_scoreboard.update_score()
    r_scoreboard.update_score()

    #Detect Collision with Paddle
    if ball.xcor() < -315 and ball.distance(lpaddle) < 50 or ball.xcor() > 315 and ball.distance(rpaddle) < 50:
        ball.bounce("horizontal")

    #Detect Collision with Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce("vertical")

    #Detect is paddle misses ball
    if ball.xcor() > 400 or ball.xcor() < -400:
        if ball.xcor() > 400:
            l_scoreboard.scored()
            if l_scoreboard.score == WINNING_SCORE:
               l_scoreboard.gameover("LEFT") 
               r_scoreboard.clear()
               game_on = False
               
        if ball.xcor() < -400:
            r_scoreboard.scored()
            if r_scoreboard.score == WINNING_SCORE:
                r_scoreboard.gameover("RIGHT")
                l_scoreboard.clear()
                game_on = False
        ball.set()










screen.exitonclick()

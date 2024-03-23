from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
turtles = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
game_is_on = True

for snakes in range(0, 3):
    snake = Turtle(shape="square", )
    snake.color("white")
    snake.penup()
    snake.setposition(starting_positions[snakes])
    turtles.append(snake)

screen.update()

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for snake in range(len(turtles) - 1, 0, -1):
        new_x = turtles[snake - 1].xcor()
        new_y = turtles[snake - 1].ycor()
        turtles[snake].goto(new_x, new_y)






















screen.exitonclick()
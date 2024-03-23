from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
turtles = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

for snakes in range(0, 3):
    snake = Turtle(shape="square", )
    snake.color("white")
    snake.penup()
    snake.setposition(starting_positions[snakes])
    turtles.append(snake)


























screen.exitonclick()
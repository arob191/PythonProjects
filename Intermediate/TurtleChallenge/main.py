from turtle import Turtle, Screen
import random

lilly = Turtle()
lilly.shape("turtle")
lilly.pensize(10)
lilly.speed(0)

color = ["green", "orange", "yellow", "blue", "pink", "purple", "black", "dark green", "gray", "red", "dark green", "crimson", "green yellow", "cornflower blue", "orange red"]

# def draw_shape(numb_sides):
#     lilly.color(random.choice(color))
#     angle = 360 / numb_sides
#     for _ in range(numb_sides):
#         lilly.forward(5)
#         lilly.right(angle)

# for i in range(3, 10):
#     draw_shape(i)

direction = [0, 90, 180, 270]

def random_walk(distance):
    for i in range(distance):
        lilly.color(random.choice(color))
        lilly.forward(30)
        lilly.setheading(random.choice(direction))


random_walk(100)

screen = Screen()
screen.exitonclick()
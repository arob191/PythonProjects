from turtle import Turtle, Screen
import random

lilly = Turtle()
lilly.shape("turtle")

color = ["green", "orange", "yellow", "blue", "pink", "purple", "black", "dark green", "gray", "red", "dark green", "crimson", "medium violet red", "green yellow", "cornflower blue", "orange red"]

def draw_shape(numb_sides):
    lilly.color(random.choice(color))
    angle = 360 / numb_sides
    for _ in range(numb_sides):
        lilly.forward(5)
        lilly.right(angle)

for i in range(359, 360):
    draw_shape(i)


screen = Screen()
screen.exitonclick()
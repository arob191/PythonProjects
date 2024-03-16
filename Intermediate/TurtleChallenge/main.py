from turtle import Turtle, Screen
import random

lilly = Turtle()
lilly.shape("turtle")
lilly.color("Green")

color = ["green", "orange", "yellow", "blue", "pink", "purple", "black", "dark green", "gray", "red"]

def draw_shape(numb_sides):
    lilly.color(random.choice(color))
    angle = 360 / numb_sides
    for _ in range(numb_sides):
        lilly.forward(100)
        lilly.right(angle)

for i in range(3, 10):
    draw_shape(i)


screen = Screen()
screen.exitonclick()
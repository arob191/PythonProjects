import colorgram
import turtle
import random

colors = colorgram.extract("dhirst.jpg", 26)
rgbs = []
painter = turtle.Turtle()
turtle.colormode(255)
painter.penup()
painter.setx(-150)
painter.sety(50)

for rgb in colors:
    first_rgb = rgb.rgb
    r = int(first_rgb.r)
    g = int(first_rgb.g)
    b = int(first_rgb.b)
    rgb_tuple = (r, g, b)
    rgbs.append(rgb_tuple)


painter.color(random.choice(rgbs))
painter.dot(50, "blue")


screen = turtle.Screen()
screen.exitonclick()
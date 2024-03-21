import colorgram
import turtle
import random

# colors = colorgram.extract("dhirst.jpg", 27)
rgbs = [(199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57), (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174), (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42), (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203), (150, 115, 120), (202, 185, 190)]
painter = turtle.Turtle()
turtle.colormode(255)
painter.penup()
painter.hideturtle()
painter.speed(0)
painter.setx(-250)
painter.sety(-250)


# for rgb in colors:
#     first_rgb = rgb.rgb
#     r = int(first_rgb.r)
#     g = int(first_rgb.g)
#     b = int(first_rgb.b)
#     rgb_tuple = (r, g, b)
#     rgbs.append(rgb_tuple)
# print(rgbs)


def make_row(times):
    for _ in range(times):
        for _ in range(10):
            painter.dot(10, random.choice(rgbs))
            painter.forward(50)
        painter.setheading(90)
        painter.forward(50)
        painter.setheading(180)
        painter.forward(500)
        painter.setheading(0)


make_row(10)


screen = turtle.Screen()
screen.exitonclick()
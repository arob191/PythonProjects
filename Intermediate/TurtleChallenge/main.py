import turtle as t
import random

lilly = t.Turtle()
lilly.shape("turtle")
lilly.pensize(10)
lilly.speed(0)
t.colormode(255)

# def draw_shape(numb_sides):
#     lilly.color(random_color())
#     angle = 360 / numb_sides
#     for _ in range(numb_sides):
#         lilly.forward(5)
#         lilly.right(angle)

# for i in range(3, 10):
#     draw_shape(i)

direction = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def random_walk(distance):
    for i in range(distance):
        lilly.color(random_color())
        lilly.forward(30)
        lilly.setheading(random.choice(direction))


random_walk(100)

screen = t.Screen()
screen.exitonclick()
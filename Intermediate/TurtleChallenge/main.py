import turtle as t
import random

lilly = t.Turtle()
lilly.shape("classic")
lilly.pensize(1)
lilly.speed(0)
t.colormode(255)
direction = [0, 90, 180, 270]
heading = 0
num_of_circles = 50

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

# Code exercise 1
def draw_shape(numb_sides):
    lilly.color(random_color())
    angle = 360 / numb_sides
    for _ in range(numb_sides):
        lilly.forward(5)
        lilly.right(angle)
# for i in range(3, 10):
#     draw_shape(i)

# Code exercise 2
def random_walk(distance):
    for i in range(distance):
        lilly.color(random_color())
        lilly.forward(30)
        lilly.setheading(random.choice(direction))
# random_walk(100)


# Code exercise 3
def repeating_circles(num_of_circles):
    angle = 360 / num_of_circles
    for _ in range(num_of_circles +1):
        lilly.color(random_color())
        lilly.circle(100)
        lilly.seth(lilly.heading() + angle)

repeating_circles(num_of_circles)

screen = t.Screen()
screen.exitonclick()
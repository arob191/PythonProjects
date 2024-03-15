from turtle import Turtle, Screen

lilly = Turtle()
lilly.shape("turtle")
lilly.color("Green")

for i in range(50):
    lilly.forward(2)
    lilly.pu()
    lilly.forward(2)
    lilly.pd()




screen = Screen()
screen.exitonclick()
from turtle import Turtle, Screen

lilly = Turtle()
lilly.shape("turtle")
lilly.color("Green")

austin = Turtle()
austin.shape("turtle")
austin.color("Red")


for i in range(4):
    lilly.forward(100)
    lilly.right(90)

for i in range(4):
    austin.forward(100)
    austin.right(90)






screen = Screen()
screen.exitonclick()
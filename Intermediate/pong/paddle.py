from turtle import Turtle
STARTING_POSITION = [(380, 20), (380, 0), (380, -20)]


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self = Turtle("square")
        self.color("white")
        self.penup()
        self.goto(350, 0)
        self.speed(5)
        self.shapesize(5, 1)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)
   
    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
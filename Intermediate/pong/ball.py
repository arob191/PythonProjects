from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.speed(4)
        self.goto(0, 0)
        self.setheading(45)
        self.x_move = 10
        self.y_move = 10

    def move(self):
        new_y = self.ycor() + self.y_move
        new_x = self.xcor() + self.x_move
        self.goto(new_x, new_y)
    
    def bounce(self, bounce):
        if bounce == "vertical":
            self.y_move *= -1
            
        if bounce == "horizontal":
            self.x_move *=-1
            if self.x_move == 0:
                self.x_move -= 3
                self.y_move -= 3
            else:
                self.x_move += 3
                self.y_move += 3

    def set(self):
        self.goto(0, 0)
        self.x_move *= -1
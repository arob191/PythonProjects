from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=275)
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.write(f"Score = {self.score}", False, align="center", font=("Fantasy"))

    def scored(self):
        self.clear()
        self.score += 1
        self.update_score()


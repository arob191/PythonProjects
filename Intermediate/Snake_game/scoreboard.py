from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

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
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def scored(self):
        self.clear()
        self.score += 1
        self.update_score()

    def gameover(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)


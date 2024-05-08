from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("black")
        self.penup()
        self.goto(x=0, y=260)
        self.hideturtle()
        self.update_score()
    
    def update_score(self):
        self.write(f"Level: {self.score}", align=ALIGNMENT, font=FONT)

    def scored(self):
        self.clear()
        self.score += 1
        self.update_score()
    
    def game_over(self):
        self.clear()
        self.goto(x=0, y=0)
        self.write(f"You lose. Your score is {self.score}", align=ALIGNMENT, font=FONT)
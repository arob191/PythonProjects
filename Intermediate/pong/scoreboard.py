from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 12, "normal")

#Need TO CHANGE THIS. This should be only one turtle and it two objects should be made on the main script.
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=-25, y=275)
        self.hideturtle()
        self.update_score()
    
    def left_board(self):
        pass

    def right_board(self):
        pass

    def update_score(self):
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)

    def scored(self, side):
        if side == "left":
            self.left_board.clear()
            self.left_board.score += 1
            self.left_board.update_score()
        
        if side == "right":
            self.right_board.clear()
            self.right_board.score += 1
            self.right_board.update_score()

    def gameover(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)
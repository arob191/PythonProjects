from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
turtles = []

class Snake:
  
  def __inut__ (self) -> None:
    for self in range(0, 3):
      self = Turtle(shape="square", )
      self.color("white")
      self.penup()
      self.setposition(starting_positions[self])
      turtles.append(self)
  
  def move(self):
    for self in range(len(turtles) - 1, 0, -1):
        new_x = turtles[self - 1].xcor()
        new_y = turtles[self - 1].ycor()
        turtles[self].goto(new_x, new_y)
    turtles[0].forward(20)

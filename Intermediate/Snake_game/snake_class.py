from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
  
  def __inut__ (self):
    self.segments = []
    self.create_snake()
  
  def create_snake(self):
     for positions in STARTING_POSITION:
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(positions)
        self.segments.append(new_segment)

  def move(self):
    for segment in range(len(self.segments) - 1, 0, -1):
       new_x = self.segments[segment - 1].xcor()
       new_y = self.segments[segment -1].ycor()
       self.segments[segment].goto(new_x, new_y)
    self.segments[0].forward(MOVE_DISTANCE)

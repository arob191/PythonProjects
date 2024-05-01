from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x = 310, y = random.randint(-300, 300))
        self.setheading(180)

    def generate_car(self):
        new_car = Turtle()
        new_car.penup()
        new_car.goto(x = 310, y = random.randint(-300, 300))
        new_car.setheading(180)
        
    
    def move(self):


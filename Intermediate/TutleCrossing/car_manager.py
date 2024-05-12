from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager():

    def __init__(self):
        self.move_distance = STARTING_MOVE_DISTANCE
        self.all_cars = []

    def generate_car(self):
        ran_chance = random.randint(1, 6)
        if ran_chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(x = 310, y = random.randint(-250, 250))
            new_car.setheading(180)
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)
    
    def move(self):
        for cars in self.all_cars:
            cars.forward(self.move_distance)
    
    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT
    
    def reset(self):
        for cars in self.all_cars:
            cars.goto(x=-350, y=350)


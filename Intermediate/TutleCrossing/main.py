import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move()
    #check if turtle collides with car
    for car in car_manager.all_cars:
        if player.distance(car) < 25:
            print("you lose")

    #check if turtle reaches finish line
    if player.ycor() > 280:
        print("Next Level")
        player.set()
        scoreboard.scored()
        car_manager.increase_speed()
        car_manager.reset()



screen.exitonclick()

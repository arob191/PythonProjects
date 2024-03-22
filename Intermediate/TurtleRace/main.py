from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make a bet", "Which Turtle Do You Think Will Win? Blue/Green/Yellow/Red/Orange/Purple: ").lower()
colors = ["blue", "green", "yellow", "red", "orange", "purple"]
start_pos = [-125, -75, -25, 25, 75, 125]
all_turtle = []


for turtle_instance in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.speed(10)
    new_turtle.color(colors[turtle_instance])
    new_turtle.goto(x=-230, y=start_pos[turtle_instance])
    all_turtle.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    
    for turtle in all_turtle:
        if turtle.xcor() >= 210:
            is_race_on = False
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"you win. The winner is the {winner} turtle.")
            else:
                print(f"you lose. The winner is the {winner} turtle.")
        

        random_dist = random.randint(0, 10)
        turtle.forward(random_dist)

screen.exitonclick()
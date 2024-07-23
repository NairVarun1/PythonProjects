from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
is_race_on = False

user_bet = screen.textinput(title="Make your bet!!", prompt="Which turtle will win? Enter a color:").lower()
colors = ["red", "orange", "yellow", "green", "blue", "violet"]


def make_turtle():
    turtles = []
    y_positions = [-100, -60, -20, 20, 60, 100]
    for index in range(6):
        new_turtle = Turtle(shape="turtle")
        new_turtle.color(colors[index])
        new_turtle.penup()
        new_turtle.goto(x=-230, y=y_positions[index])
        turtles.append(new_turtle)
    return turtles


turtles = make_turtle()

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet:
                print(f"You've won! The winning turtle is {winning_color.upper()}")
            else:
                print(f"You've lost! The winning turtle is {winning_color.upper()}")
            break
        else:
            distance = random.randint(10, 20)
            turtle.forward(distance)

screen.exitonclick()

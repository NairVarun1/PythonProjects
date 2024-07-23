from turtle import Screen
from player import Player
from score import Score
from carmanager import CarManager
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Score()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score.game_over()

    if player.is_at_finish_line():
        score.add_score()
        player.goto_start()
        car_manager.level_up()

screen.exitonclick()

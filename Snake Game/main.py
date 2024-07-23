from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Collision Detection with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.increase_score()

    #Collision detection with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    #Collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

screen.exitonclick()

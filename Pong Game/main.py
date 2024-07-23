from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((380, 0))
l_paddle = Paddle((-380, 0))
ball = Ball()
score = Score()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddles
    if ball.xcor() > 340 and ball.distance(r_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() < -340 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # Detect when the ball goes out of bounds
    if ball.xcor() > 390:
        ball.reset()
        score.l_point()

    if ball.xcor() < -390:
        ball.reset()
        score.r_point()

screen.exitonclick()

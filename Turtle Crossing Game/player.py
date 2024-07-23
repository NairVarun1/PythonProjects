from turtle import Turtle

START = (0, -280)
FINISH_LINE = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('black')
        self.setheading(90)
        self.goto_start()

    def go_up(self):
        self.forward(10)

    def goto_start(self):
        self.goto(START)

    def is_at_finish_line(self):
        return self.ycor() > FINISH_LINE

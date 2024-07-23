from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(-240, 250)
        self.update_score()

    def add_score(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level : {self.score}", align="left", font=("Arial", 20, "bold"))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over !", align="center", font=("Arial", 20, "bold"))

from turtle import Turtle


SCORE = 0

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.ht()
        self.goto(x=0, y=270)
        self.write(f"score: {SCORE}", align="center", font=('Arial', 15, 'normal'))

    def new_score(self):
        global SCORE
        SCORE += 1
        self.clear()
        self.write(f"score: {SCORE}", align="center", font=('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game over", align="center", font=('Arial', 15, 'normal'))














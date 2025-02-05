from turtle import Turtle

ALLIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}",align= ALLIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over", align="Center", font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
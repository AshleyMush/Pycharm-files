
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("orange")
        self.score = 0
        self.level = 1


        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-200, -300)
        self.write(f"Score:{self.score}", align="center", font=("Courier", 30, "normal"))

        self.goto(-250, 250)
        self.write(f"Level:{self.level}", align="center", font=("Courier", 15, "bold"))

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", move= False, align="Center", font=("Arial", 10, "bold"))


from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-230,260)
        self.score = 0
        self.write(arg=f"Score:{self.score}", move= False, align="center", font=("arial", 20, "normal"))
        #Highest score
        self.highest_score = 0
        self.score_bank = []
        self.goto(180, 260)
        self.write(arg=f"Highest Score {self.highest_score}", move=False, align="center", font=("arial", 18, "normal"))





    def add_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score:{self.score}", move= False, align="center", font=("arial", 24," normal"))

    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", move= False, align="Center", font=("Arial", 10, "bold"))

    def save_previous_score(self):
        #Add the score to the bank
        self.score_bank.append(self.score)

    def find_highest_score(self):

#Go through all the scores in the score bank
        for any_score in self.score_bank:
            if any_score > self.highest_score:
                self.highest_score = any_score









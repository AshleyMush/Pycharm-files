from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")





class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data", mode="r") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()

        self.write(f"Score: {self.score} High Score {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0

            # #CREATING FILE FOR HIGHSCORE AND APPENDING TO IT
            with open("data", mode="w") as data:
                data.write(f"{self.high_score}")

            self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


"""

score_file will take high score int
TODO: we need to create a list in score_file
highest_score = 0
 for a_score in score_file_list:
 if a_score > highest_score
 highest_score = score
     
"""








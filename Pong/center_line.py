from turtle import Turtle

class Center_Line(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0,295)
        self.pensize(10)
        self.draw_center_line()
        self.pencolor("black")



    def draw_center_line(self):
        self.pendown()
        self.goto(0,-295)

    def change_colour(self):
        self.pencolor("red")

    def normal_colour(self):
        self.pencolor("black")



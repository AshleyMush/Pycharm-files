from turtle import Turtle




class Walls(Turtle):
    def __init__(self):
        super().__init__()
        self.pensize(10)
        self.penup()
        self.hideturtle()
        # vertical left line
        self.setposition(-295, 295)

        self.pendown()
        self.goto((-295, -295))

        # Horizontal
        self.goto((295, -295))

        # right vertical
        self.goto(295, 295)

        # top horizontal
        self.goto(-295, 295)






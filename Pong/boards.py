from turtle import Turtle, Screen

class Board(Turtle ):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")




    def go_up(self):
        new_y = self.ycor() + 30
        #Go to curremt x
        self.goto(self.xcor(),new_y )

    def go_down(self):
        new_y = self.ycor() - 30
        #Go to curremt x
        self.goto(self.xcor(),new_y )















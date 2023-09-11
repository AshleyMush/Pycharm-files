import turtle
from turtle import Turtle




class Walls(Turtle):
    def __init__(self):
        super().__init__()

        self.left_wall()
        self.right_wall()
        self.top_wall()
        self.bottom_wall()



      

    def left_wall(self):
        self.left_wall = Turtle()
        self.left_wall .shape("square")
        self.left_wall.penup()
        self.left_wall .color("white")


        self.left_wall .goto(-395,0)

        self.left_wall .shapesize(stretch_wid=30, stretch_len=0.2)

    def right_wall(self):
        self.right_wall = Turtle()
        self.right_wall.shape("square")
        self.right_wall.color("white")
        self.right_wall.penup()
        self.right_wall.goto(390, 0)



        self.right_wall.shapesize(stretch_wid=30, stretch_len=0.2)

    def bottom_wall(self):

        self.bottom_wall = Turtle()
        self.bottom_wall.setheading(90)
        self.bottom_wall.shape("square")
        self.bottom_wall.color("white")
        self.bottom_wall.penup()
        self.bottom_wall.goto(0, -290)

        self.bottom_wall.shapesize(stretch_wid= 40, stretch_len=0.2)


    def top_wall (self):


        self.top_wall  = Turtle()
        self.top_wall .setheading(90)
        self.top_wall .shape("square")
        self.top_wall .color("white")
        self.top_wall.penup()
        self.top_wall .goto(0, 295)


        self.top_wall .shapesize(stretch_wid= 40, stretch_len=0.2)


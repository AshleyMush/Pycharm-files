from turtle import Turtle, Screen
import random


tim = Turtle()

class Shape_Generator:
    def __init__(self, sides):
        self.sides = sides
        # Generate random RGB values
        self.red = random.random()
        self.green = random.random()
        self.blue = random.random()

    def angle_num(self):
        return 360 / self.sides

    def draw_shape(self):
        total_angles = self.angle_num()
        current_shape_angles = round(total_angles)

        for _ in range(self.sides):
            tim.pencolor(self.red,self.green,self.blue)
            tim.forward(100)
            tim.right(360 / self.sides)
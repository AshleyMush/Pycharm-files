from turtle import Turtle, Screen
from  my_module import *
import random


tim = Turtle()
tim.hideturtle()




#Initial shape
n = 2

for so_many_times in range(8):
    n +=1

# Create an instance of the Shape_Generator class
    current_shape = Shape_Generator(n)
    # Call the draw_shape() method
    current_shape.draw_shape()





#current_shape_angles =round(current_shape.get_angle())









screen = Screen()
screen.exitonclick()
import turtle
from turtle import  Turtle, Screen
import random


turtle.colormode(255)
ash = Turtle()

colour_list = [ (208, 160, 101), (150, 75, 37), (231, 213, 97), (245, 251, 247), (242, 247, 250), (132, 34, 21), (191, 156, 15), (87, 33, 21), (238, 174, 153), (21, 57, 80), (41, 117, 63), (31, 93, 135), (196, 98, 88), (2, 81, 115), (10, 99, 77), (194, 163, 165), (109, 159, 185), (73, 76, 40), (179, 209, 168), (106, 140, 129), (37, 27, 35), (78, 153, 168), (46, 50, 47), (134, 163, 150), (234, 178, 180), (2, 72, 136), (125, 64, 66), (118, 36, 39)]


print(ash.position())

def random_colour():
    random_colour = random.choice(colour_list)
    return random_colour





def straight_line():
    for _ in range(9):
        #      size  color
        ash.dot(20, random_colour() )
        ash.penup()
        ash.fd(50)
        ash.dot(20, random_colour() )

n =0
for _ in range(10):
    n += 50

    straight_line()
    ash.goto(0, n)
    straight_line()







screen = Screen()
screen.exitonclick()
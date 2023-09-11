import another_module
from  turtle import Turtle, Screen

print(another_module.another_variable)
#       Module
import  turtle
'''
import module

class = Object()





'''
# #     Module.Class() - in PascalCase e.g This_Class()
# '''
# print(turtle.Turtle())
# '''
#
#
# #Turn it into an object
#
# ashley_object = Turtle()
# ashley_object.shape("turtle")
# turtle.forward(250)
# turtle.goto(25,100)
# turtle.circle(200)
# turtle.pen(pencolor="green", fillcolor="red", pensize= 100)
#
# print(ashley_object)
#
# my_screen = Screen()
# #      Object  . method
# print(my_screen.canvheight)
#
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

print(table)
#Adding Columns
table.add_column("Pokemon name", ["Pikachu" , "Squartle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_column("Value", ["$100", "$55, $109"])
table.align = "l"
print(table.align)

table.format = True


print(table)

#NO BORDERS
table.border = False


print(table)

#Sorting

print(table.get_string(sortby = "Value"))
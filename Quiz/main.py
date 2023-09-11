import turtle
from turtle import Screen, Turtle
import time
screen = Screen()
screen.setup(width=600, height=600)
#screen.bgpic("C:/Users/Ashley/Pictures/snake1.png")
screen.bgcolor("black")
screen.title("My Snake Game")
snake = Turtle()


#1st square is 20px (0,0) then left then left

starting_position = [(0,0), (-20,0), (-40,0)]
#removes frame by frame lag
screen.tracer(0)
segments= []
snake.hideturtle()

for position in starting_position:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()

    new_segment.goto(position)
    segments.append(new_segment)

screen.update()

#Moving the snake forward
game_is_on = True
while game_is_on:
    for seg in segments:
        seg.forward(20)
        time.sleep(1)

#Put it in a list and move list in an index[0]

screen.exitonclick()

turtle.done()
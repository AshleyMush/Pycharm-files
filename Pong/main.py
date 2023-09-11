from turtle import Turtle, Screen
from walls import Walls
from center_line import Center_Line
from boards import Board
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=800, height=600)
# screen.bgcolor("green")
screen.bgpic("C:/Users/Ashley/Pictures/grass2.png")

screen.title("My Pong Game")
screen.tracer(0)

line = Center_Line()
line.draw_center_line()

ball = Ball()
scoreboard = Scoreboard()




walls = Walls()

left_board = Board((-350, 0))
right_board = Board((350, 0))




screen.listen()
screen.onkey(left_board.go_up, "w")
screen.onkey(left_board.go_down, "s")
screen.onkey(right_board.go_up, "Up")
screen.onkey(right_board.go_down, "Down")




game_is_on = True

while game_is_on:
    time.sleep(0.001)
    screen.update()
    time.sleep(0.1)
    ball.move()




#Detecting collision with wall
    # if ball.ycor() > 275 or ball.ycor() < -275:
        #It needs to bounce
    # Detecting collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275  and ball.ycor() < -275 or ball.ycor() > 275 :
        # It needs to bounce
        ball.bounce_Y()

    #Detect collision with R paddle
    if ball.distance(right_board) < 50 and ball.xcor() > 330 or ball.distance(left_board) < 50 and ball.xcor() < -330:
        ball.bounce_X()



#     IF R paddle misses
    if ball.xcor() > 380 :
        ball.reset_position()
        scoreboard.l_point()
#   If L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()










screen.update()
screen.exitonclick()


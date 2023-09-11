import turtle
from walls import Walls
from scoreboard import Scoreboard
from turtle import Screen
import time
from snake import Snake
from food import Food
screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("C:/Users/Ashley/Pictures/snake1.png")
#screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


walls = Walls()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




#Moving the snake forward
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
#                     len(segments) to access the last element of a list
    snake.move()


    scoreboard.find_highest_score()

#Detect food coliding with snake
    #If snake head is < 15 from the food
    if snake.head.distance(food) < 20:
        print("Snake Colided with Food")
        food.refresh()
        snake.extend()
        scoreboard.add_score()





    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:

        scoreboard.save_previous_score()#Saving the previous score

        game_is_on = False
        turtle.write(arg="Game Over", move= False, align="Center", font=("Arial", 10, "bold"))

    #Detect collision with tail
    #If head collides with any segments
    #trigger game over

    # 1st seg = segments[0]   snake.head = segments[0]
    for segment in snake.segments[1::]:
        #By passing the snake head since its the first segment in segments

        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()






#Put it in a list and move list in an index[0]

screen.exitonclick()

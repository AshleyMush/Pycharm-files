from grids import Grid
import time
from turtle import Screen
from player import Player
from car_manager import CarManager, MOVE_INCREMENT, STARTING_MOVE_DISTANCE
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)



# grid = Grid()
# screen = grid.getscreen()
# grid.draw_grid(600)

scoreboard = Scoreboard()

player = Player()
screen.listen()
screen.onkey(player.move, "Up")

carmanager = CarManager()


#Detect if turtle has passed finishing line
# if player.ycor() > 280:
#     print("PASSED")
# print(player.ycor())




game_is_on = True
while game_is_on:
    time.sleep(0.1)#TODO HERE
    screen.update()
    carmanager.create_car()
    carmanager.move_cars()

    # Detect if turtle has passed finishing line
    #TODO REDUCE TIME.SLEEP EVERY TIME THEY CROSS
    if player.ycor() > 280:
        #If the player reaches the finishing line then we add the move increment
        carmanager.increase_car_speed()
        scoreboard.add_point()
        scoreboard.increase_level()
        player.reset_position()

    #Detect if player collides with car

    # Detect if player collides with car
    for car in carmanager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False





screen.exitonclick()
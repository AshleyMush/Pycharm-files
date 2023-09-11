from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()

            new_car.penup()
            new_car.shape("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.random_colour = random.choice(COLORS)
            new_car.color(f"{new_car.random_colour}")
            new_car.setheading(180)
            random_y = random.randint(-270, 270)
            new_car.goto(400, random_y)
            self.all_cars.append(new_car)


    def move_cars(self):
        for car in self.all_cars:
            car.forward(self.move_distance)


    def increase_car_speed(self):

        for car in self.all_cars:
            self.move_distance += 1
            car.forward(self.move_distance)






# import time
# from turtle import Turtle, Screen
# import random
#
# COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
# MOVE_INCREMENT = 10
#
# CAR_SPEED = 5  # Adjusted for smooth animation
#
#
# class CarManager():
#     def __init__(self):
#         self.cars = []
#
#     def create_cars(self):
#         for _ in range(5):
#             car = Turtle()
#             car.hideturtle()
#             car.penup()
#             car.shape("square")
#             car.penup()
#             car.shapesize(stretch_wid=1.5, stretch_len=3)
#             car.random_colour = random.choice(COLORS)
#             car.color(f"{car.random_colour}")
#             car.setheading(180)
#             self.random_position(car)
#             car.showturtle()
#             self.cars.append(car)
#
#     def random_position(self, car):
#         random_y = random.randint(-270, 270)
#         random_x = random.randint(300, 450)
#         car.setposition(random_x, random_y)
#
#     def move_cars(self):
#         for car in self.cars:
#             car.forward(CAR_SPEED)
#
#     def generate_new_cars(self):
#         for _ in range(1000):
#             self.create_cars()
#             self.move_cars()
#
#
# screen = Screen()
# screen.setup(600, 600)
# screen.tracer(0)  # Turn off automatic updates
#
# car_manager = CarManager()
#
# game_is_on = True
# while game_is_on:
#     screen.update()  # Manually update the screen
#
#     car_manager.generate_new_cars()
#     time.sleep(0.01)
#
# screen.exitonclick()
import random
from turtle import Turtle, Screen
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

class Car_Manager():
    def __init__(self):
        self.garage = []
        self.make_car()




    def make_car(self):
        new_car = Turtle("square")
        new_car.penup()
        random_colour = random.randrange(0,6)
        new_car.color(COLORS[random_colour])
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.random_colour = random.choice(COLORS)
        new_car.color(f"{new_car.random_colour}")
        new_car.setheading(180)
        random_y = random.randint(-270, 270)
        new_car.goto(400, random_y)
        self.garage.append(new_car)

    def move_cars(self):
        for car in self.garage:
            car.forward(10)








screen = Screen()
car_manager = Car_Manager()


while True:
    car_manager.make_car()
    car_manager.make_car()









screen.exitonclick()

import  turtle as t
import random

tim = t.Turtle()


#Using a tuple to generate random RGB int

red = random.random()
green = random.random()
blue = random.random()

#Defining random pen colour

t.colormode(255)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colour = (r, g, b)



    return random_colour


tim.pensize(20)
tim.speed("fast")

for _ in range(200):
    directions = [0, 90, 180, 270]

#             r = 56 g= 45 b =17
    tim.color(random_colour())

    tim.forward(30)
    tim.setheading(random.choice(directions))


screen = t.Screen()

screen.exitonclick()

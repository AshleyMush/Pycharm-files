
import turtle as t
import  random


#Define obj
ash = t.Turtle()

ash.home()

#Tapping into the module to adjust colour mode
t.colormode(255)
ash.speed("fastest")



def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)

    #Random colour tuple
    random_colour = (r, g, b)



    return random_colour

def draw_sprirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        ash.setheading(ash.heading() + size_of_gap)
        ash.circle(100)

        ash.color(random_colour())




draw_sprirograph(5)

screen = t.Screen()
screen.exitonclick()
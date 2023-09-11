from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def move_back():
 tim.back(10)


def move_counter_clock_wise():
 tim.left(10)

def move_clock_wise():
 tim.right(10)

def clear_screen():
    tim.reset()
screen.listen()

#        keyboard key     function
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun= move_back)
screen.onkey(key="a", fun= move_counter_clock_wise)
screen.onkey(key="d", fun=move_clock_wise)
screen.onkey(key="c", fun=clear_screen)






screen.exitonclick()


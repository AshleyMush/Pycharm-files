from turtle import Turtle, Screen

class Ball(Turtle):
    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.x_move = 20
        self.y_move = 20
        self.move_speed = 0.1



    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x,new_y)



    def reset_position(self):
        self.home()
        self.move_speed = 0.1
        self.bounce_X()


    def bounce_Y(self):
        #We multiply the y move to negative so that when it collides with wall it begins to decrease value
        self.y_move *= -1

    def bounce_X(self):
        #We multiply the y move to negative so that when it collides with wall it begins to decrease value
        self.x_move *= -1
        self.move_speed * 0.9



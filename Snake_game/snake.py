import turtle
from turtle import Turtle, Screen

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP_ANGLE = 90
DOWN_ANGLE = 270
LEFT_ANGLE = 180
RIGHT_ANGLE = 0



class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()

        self.head = self.segments[0]





    def create_snake(self):
        #               [(0, 0), (-20, 0), (-40, 0)]
        for position in STARTING_POSITION:
            self.add_segment(position)


    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        #                (0, 0)
        new_segment.goto(position)
        self.segments.append(new_segment)



    def extend(self):
        # add new segment to snake                     0        1 or -2          2 or -1
        #Getting hold of the last indez in segments [(0, 0), (-20, 0), 😜(-40, 0)]
        self.add_segment(self.segments[-1].position())#Getting hold of the last index in lists

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def down(self):
        if self.head.heading() != UP_ANGLE:
            self.head.setheading(DOWN_ANGLE)#270

    def up(self):
        if self.head.heading() != DOWN_ANGLE:
            self.head.setheading(UP_ANGLE)#90

    def left(self):
        if self.head.heading() != RIGHT_ANGLE:
            self.head.setheading(LEFT_ANGLE)#180

    def right(self):
        if self.head.heading() != LEFT_ANGLE:
            self.head.setheading(RIGHT_ANGLE)#0





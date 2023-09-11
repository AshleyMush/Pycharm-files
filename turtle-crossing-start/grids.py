from turtle import Turtle

class Grid(Turtle):
    def __init__(self):
        super().__init__()
        self.speed(0)  # Set the turtle's speed to the fastest
        self.hideturtle()  # Hide the turtle's shape

    def draw_grid(self, size):
        self.penup()
        self.goto(-size // 2, -size // 2)  # Start at the bottom-left corner
        self.pendown()
        self.setheading(0)  # Face right

        # Draw the vertical lines
        for _ in range(size // 20 + 1):
            self.forward(size)
            self.penup()
            self.backward(size)
            self.left(90)
            self.forward(20)
            self.right(90)
            self.pendown()

        self.penup()
        self.goto(-size // 2, -size // 2)  # Reset position
        self.setheading(90)  # Face upward
        self.pendown()

        # Draw the horizontal lines
        for _ in range(size // 20 + 1):
            self.forward(size)
            self.penup()
            self.backward(size)
            self.right(90)
            self.forward(20)
            self.left(90)
            self.pendown()

        self.penup()  # Lift the pen after drawing the grid

        # Draw y-axis
        self.goto(0, -size // 2)
        self.pendown()
        self.color("blue")
        self.forward(size)
        self.write("300", align="right", font=("Arial", 14, "bold")) #TODO WRITE Y AXIS
        self.penup()

        # Draw x-axis
        self.goto(-size // 2, 0)
        self.setheading(0)
        self.pendown()
        self.color("red")
        self.forward(size)
        self.write(" 300", align="right", font=("Arial", 14, "bold")) #TODO WRITE X AXIS
        self.penup()
#
# # Create an instance of the Grid class
# grid = Grid()
#
# # Set up the turtle window
# screen = grid.getscreen()
# screen.setup(650, 650)  # Set the window size
# screen.bgcolor("white")  # Set the background color
#
# # Draw the grid
# grid.draw_grid(600)
#
# # Keep the turtle window open until it is manually closed
# screen.mainloop()

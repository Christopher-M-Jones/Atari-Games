from turtle import Turtle


class Lane(Turtle):
    def __init__(self):
        super(Lane, self).__init__()
        self.hideturtle()
        self.color("yellow")
        self.shapesize(stretch_len=2)

    def create_lane(self):
        self.setheading(180)
        self.penup()
        self.goto(280, 0)
        for _ in range(10):
            self.create_line()
            self.create_space()

    def create_line(self):
        self.pendown()
        self.forward(30)

    def create_space(self):
        self.penup()
        self.forward(30)

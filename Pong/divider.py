from turtle import Turtle


class Divider(Turtle):
    def __init__(self):
        super(Divider, self).__init__()
        self.hideturtle()
        self.color("white")
        self.shapesize(stretch_len=2)

    def create_lane(self):
        self.setheading(270)
        self.penup()
        self.goto(0, 290)
        for _ in range(30):
            self.create_line()
            self.create_space()

    def create_line(self):
        self.pendown()
        self.forward(10)

    def create_space(self):
        self.penup()
        self.forward(10)


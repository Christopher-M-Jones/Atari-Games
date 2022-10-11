from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.penup()
        self.goto(location)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=3, stretch_len=1)

    def move_up(self):
        new_y_position = self.ycor() + 20
        self.goto(self.xcor(), new_y_position)

    def move_down(self):
        new_y_position = self.ycor() - 20
        self.goto(self.xcor(), new_y_position)

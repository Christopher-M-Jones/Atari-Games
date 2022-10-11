from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
BOTTOM_OF_SCREEN = -260


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto_start()

    def move_forward(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_backward(self):
        if not self.ycor() < BOTTOM_OF_SCREEN:
            self.setheading(270)
            self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def level_up(self):
        self.level += 1

    def cross_finish_line(self):
        if self.ycor() > 280:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(STARTING_POSITION)

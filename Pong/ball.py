from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.penup()
        self.goto(0, 0)
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.x_move = 1
        self.y_move = 1.33

    def change_direction(self):
        pass

    def move(self):
        new_x_coordinate = self.xcor() + self.x_move
        new_y_coordinate = self.ycor() + self.y_move
        self.goto(new_x_coordinate, new_y_coordinate)

    def bounce_y_axis(self):
        self.y_move *= -1

    def bounce_x_axis(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x_axis()

    def increase_speed(self):
        self.x_move *= 2
        self.y_move *= 2



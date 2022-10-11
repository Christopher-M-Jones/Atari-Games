from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 2


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        chance_to_create = randint(1, 5)
        if chance_to_create == 1:
            new_car = Turtle("square")
            new_car.color(choice(COLORS))
            new_car.shapesize(stretch_len=2)
            new_car.speed = self.speed
            new_car.setheading(180)
            new_car.penup()
            y_coordinate = self.y_coordinate()
            new_car.goto(300, y_coordinate)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(car.speed)

    def increase_speed(self):
        self.speed += MOVE_INCREMENT

    def y_coordinate(self):
        if not self.cars:
            return randint(-250, -20)
        else:
            if self.cars[-1].ycor() > 0:
                return randint(-250, -20)
            else:
                return randint(20, 250)

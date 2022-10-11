from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270


class Snake:
    def __init__(self):
        self.segments = []
        self.create()
        self.head = self.segments[0]

    def create(self):
        """Create starting values for turtles in snake body"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """add segment to snake body"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def move(self):
        """Move snake head and update segment positions"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()

            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """turn snake head up"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """turn the snake head down"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """turn the snake head left"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """turn the snake head right"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def grow(self):
        """add a new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create()
        self.head = self.segments[0]



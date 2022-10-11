from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
from divider import Divider

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

game_on = True

left_paddle = Paddle((-350, 0))
right_paddle = Paddle((350, 0))
ball = Ball()
score = Score()
divider = Divider()

divider.create_lane()

screen.listen()
screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

while game_on:
    # time.sleep(0.1)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y_axis()

    # Detect collision with left or right paddles
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (
            ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x_axis()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.left_point()

    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.right_point()

screen.exitonclick()

from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 24, 'normal')
SCORE_POSITION = (-230, 270)
HIGH_SCORE_POSITION = (170, 270)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = int(self.read_high_score())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def increase_score(self):
        """iterate current score"""
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        """update current displayed score"""
        self.clear()
        self.goto(SCORE_POSITION)
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(HIGH_SCORE_POSITION)
        self.write(f"High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_score(self):
        """reset current score and update high score"""
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.update_scoreboard()

    def write_high_score(self):
        """write high score to file highScore.txt"""
        with open("highScore.txt", mode="w") as file:
            file.write(f"{self.high_score}")

    def read_high_score(self):
        """read high score from file highScore.txt"""
        with open("highScore.txt", mode="r") as file:
            high_score = file.read()
            return high_score

from turtle import *

ALIGN = 'center'
FONT = ("Korea", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def update(self):
        self.goto(0,270)
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"Game Over!", align=ALIGN, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.update()
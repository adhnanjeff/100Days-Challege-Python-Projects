from turtle import *
from Ball import Ball  # Assuming Ball is a custom class defined in Ball.py
import time

from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)  
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))


    def l_points(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_points(self):
        self.r_score += 1
        self.update_scoreboard()

UP = 90
DOWN = 180
game_is_on = True
points1 = 0
points2 = 0

def go_upp1():
    new_y = p1.ycor() + 20
    if new_y < 300:  
        p1.goto(p1.xcor(), new_y)

def go_downp1():
    new_y = p1.ycor() - 20
    if new_y > -300: 
        p1.goto(p1.xcor(), new_y)

def go_upp2():
    new_y = p2.ycor() + 20
    if new_y < 300:  
        p2.goto(p2.xcor(), new_y)

def go_downp2():
    new_y = p2.ycor() - 20
    if new_y > -300:
        p2.goto(p2.xcor(), new_y)

screen = Screen()
screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)
c = Turtle()
sco = Score()

p1 = Turtle("square")
p1.color("white")
p1.shapesize(stretch_wid=5, stretch_len=1)
p1.penup()
p1.goto(350, 0)

p2 = Turtle("square")
p2.color("white")
p2.shapesize(stretch_wid=5, stretch_len=1)
p2.penup()
p2.goto(-350, 0)

b = Ball()  # Create an instance of the Ball class

c.left(UP)
for _ in range(15):
    c.forward(10)
    c.color("white")
    c.forward(10)
    c.color("black")

c.right(DOWN)
for _ in range(30):
    c.forward(10)
    c.color("white")
    c.forward(10)
    c.color("black")

screen.onkey(go_upp1, "Up")
screen.onkey(go_downp1, "Down")
screen.onkey(go_upp2, "w")
screen.onkey(go_downp2, "s")

while game_is_on:
    time.sleep(0.05)
    screen.update()
    b.move_ball()

    if b.ycor() > 280 or b.ycor() < -280:
        b.bounce_y()
    if (b.distance(p1) < 50 and b.xcor() > 320) or (b.distance(p2) < 50 and b.xcor() < -320):
        b.bounce_x() 
    if b.xcor() > 400: 
        b.reset()
        sco.l_points()
    if b.xcor() < -400: 
        b.reset()
        sco.r_points()

screen.exitonclick()

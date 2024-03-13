from turtle import *
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.ref()

    def ref(self):
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x, y)
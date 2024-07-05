import turtle as t
import random

def colorChoice():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255) 
    return (r, g, b)

i = t.Turtle()
i.speed("fastest")
t.colormode(255)
i.hideturtle()

i.penup()
i.setheading(225)
i.forward(300)
i.setheading(0)
number_dots = 100

for row in range(1, number_dots+1):
    i.dot(20, colorChoice())
    i.forward(50)

    if row % 10 == 0:
        i.setheading(90)
        i.forward(50)
        i.setheading(180)
        i.forward(500)
        i.setheading(0)

s = t.Screen()
s.exitonclick()

from turtle import *
import random

screen = Screen()
screen.setup(width = 500, height = 400)
screen.bgcolor("black")
user = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter the color: ").lower()
colors = ["red", "green", "blue", "pink", "purple", "orange"]
y_pos = [-70, -40, -10, 20, 50, 80]
is_race_on = False
all_turtle = []

for i in range(0, 6):
    tim = Turtle(shape="turtle")
    tim.penup()
    tim.color(colors[i])
    tim.goto(x = -230, y = y_pos[i])
    all_turtle.append(tim)  

if user:
    is_race_on = True

while is_race_on:
    for i in all_turtle:
        if i.xcor() > 230:
            is_race_on = False
            winning_color = i.pencolor()
            if winning_color == user:
                print(f"You won! The {winning_color} tutle is the winner!")
            else:
                print(f"You lost! The {winning_color} tutle is the winner!")

        random_distance = random.randint(0, 10)
        i.forward(random_distance)

        



screen.exitonclick()

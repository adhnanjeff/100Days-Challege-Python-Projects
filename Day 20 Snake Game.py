from turtle import Turtle, Screen
from snake import Snake
import time

# Initialize the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0) # This is correct, but it's not necessary here since we're not drawing anything yet


snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True 
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
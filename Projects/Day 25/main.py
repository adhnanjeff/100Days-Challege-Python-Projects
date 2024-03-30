import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "Base/Projects/Day 25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

def get_mouse_click_coor(x, y):
    print(x,y)

data = pandas.read_csv("Base/Projects/Day 25/50_states.csv")
all_states = data["state"].to_list()

guessed_states = []


while len(guessed_states) < 50:
    ans = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another states name?").title()

    if ans == "Exit":
        missed_states = [state for state in all_states if state not in guessed_states]

#       missed_states = []
#       for state in all_states:
#           if state not in guessed_states:
#                missed_states.append(state)

        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("Base/Projects/Day 25/missed_states.csv", index=False)
        break

    if ans in all_states:
        guessed_states.append(ans)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == ans]
    
        t.goto(int(state_data.x), int(state_data.y))
        t.write(ans)
    

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()
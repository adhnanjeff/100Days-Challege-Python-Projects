#This code is the answer to the Reboorgs Worlds Final Maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while is_facing_north() and wall_in_front():
    turn_right()
    
while front_is_clear():
    move()
turn_left()    

while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif right_is_clear() and not wall_in_front():  
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
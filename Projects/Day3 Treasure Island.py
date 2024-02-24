

print("Welcome to Treasure Island")
print("Your mission is to find the Treasure!")

first = input("Do you want to turn left or right? ")

if first.lower() == "right": 
    print("Game Over!")
else:
    dec = input("There is a lake in front of you. Do you want to swim or wait? ")
    if dec.lower() == "swim":
        print("Game Over!")
    else:
        door = input('Now you are in front of three houses with their doors colored "Red", "Blue", "Yellow". ')   
        if door.lower() == "yellow":
            print("You Win!")
        else:
            print("Game Over!")

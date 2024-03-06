import random
import gameData

def format_data(acc1):
    acc1_name = acc1["name"]
    acc1_decription = acc1["description"]
    acc1_counrty = acc1["country"]

    return f"{acc1_name} a {acc1_decription} from {acc1_counrty} "

print(''' 
        _       _                   __                        
  /\  /(_) __ _| |__   ___ _ __    / /  _____      _____ _ __ 
 / /_/ / |/ _` | '_ \ / _ \ '__|  / /  / _ \ \ /\ / / _ \ '__|
/ __  /| | (_| | | | |  __/ |    / /__| (_) \ V  V /  __/ |   
\/ /_/ |_|\__, |_| |_|\___|_|    \____/\___/ \_/\_/ \___|_|   
          |___/                                              
''')

game_On = True
score = 0
acc2 = random.choice(gameData.data)

while game_On:
    acc1 = acc2
    acc2 = random.choice(gameData.data)
    
    if acc1 == acc2:
        acc2 = random.choice(gameData.data)

    print(f"Compare A: {format_data(acc1)}.")

    print(''' 
    /\   /\___ 
    \ \ / / __|
     \ V /\__ \
      \_/ |___/
    ''')

    print(f"Compare B: {format_data(acc2)}.")

    guess = input("Enter 'A' or 'B' ").lower().strip()

    if guess == "a":
        if acc1["follower_count"] > acc2["follower_count"]:
            score += 1
            print("You guessed it right")
        else:
            print(f"You guessed it wrong, your final score is {score}")
            game_On = False
            score = 0

    elif guess == "b":
        if acc1["follower_count"] < acc2["follower_count"]:
            score += 1
            print("You guessed it right")
        else:
            print(f"You guessed it wrong, your final score is {score}")
            game_On = False
            score = 0
        

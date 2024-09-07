#There seems to be few errors in this code try figuring ot out, I'll try to figure it out as soon as possible
import random
from replit import clear

stages = ['''
    _ _ _ _ _ _ _ _
      
       +------+
       |      |
       O      |
      /|\     |
      / \     |
              |
    ==============
''',
''' 
    _ _ _ _ _ _ _ _
      
       +------+
       |      |
       O      |
      /|\     |
      /       |
              |
    ==============
''',
''' 
    _ _ _ _ _ _ _ _
      
       +------+
       |      |
       O      |
      /|\     |
              |
              |
    ==============
''',
''' 
    _ _ _ _ _ _ _ _
      
       +------+
       |      |
       O      |
      /|      |
              |
              |
    ==============
''',
''' 
    _ _ _ _ _ _ _ _
      
       +------+
       |      |
       O      |
       |      |
              |
              |
    ==============
''',
''' 
       +------+
       |      |
       O      |
              |
              |
              |
    ==============
'''
]

logo = ''' 
     _                                             
    | |                                            
    | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
    | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                       |___/                      
'''

word_list = ["India", "America", "Japan"]
chosen_word = random.choice(word_list)
word_len = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
display = [] * word_len

for i in range(word_len):
    display += "_"

while not end_of_game:
    guess = input("Guess a character: ").lower()
    clear()

    if guess in display:
        print(f"You have already guessed {guess}")
    
    for pos in range(word_len):
        letter = chosen_word[pos]
        if letter == guess:
            display[pos] = letter
        
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lost a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You're out of lives. You lose.")

    print(" ".join(display))

    if "_" not in display:
        end_of_game = True
        print(f"You got it! The word was {chosen_word}")

    print(stages[lives-1])

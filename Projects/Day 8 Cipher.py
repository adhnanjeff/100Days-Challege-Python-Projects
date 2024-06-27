print(''' 
    ___ __ _  ___  ___  __ _ _ __ 
 / __/ _` |/ _ \/ __|/ _` | '__|
| (_| (_| |  __/\__ \ (_| | |   
 \___\__,_|\___||___/\__,_|_| 
      _       _               
     (_)     | |              
  ___ _ _ __ | |__   ___ _ __ 
 / __| | '_ \| '_ \ / _ \ '__|
| (__| | |_) | | | |  __/ |   
 \___|_| .__/|_| |_|\___|_|   
       | |                    
       |_|       
''')

alphas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

choice = input('Type "Encode" to encrypt or type "Decode" to decrypt \n').lower()



def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphas.index(letter)
        new_position = (position + shift) % 26
        new_letter = alphas[new_position]
        cipher_text += new_letter

    print(f"The encoded text is {cipher_text}")

def decrypt(text, shift):
    codeWord = ""
    for letter in text:
        position = alphas.index(letter)
        new_position = (position - shift) % 26
        new_letter = alphas[new_position]
        codeWord += new_letter

    print(f"The encoded text is {codeWord}")         

if choice == "encode":
    word = input('Type the word to encrypt\n')
    shift = int(input("Type the shift number: "))
    encrypt( word,shift)

elif choice == "decode":
    word = input('Type the word to decrypt\n')
    shift = int(input("Type the shift number: "))
    decrypt(word,shift)        

else:
    print('Please enter a valid choice, either "Encode" or "Decode" ')    

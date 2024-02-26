import random

def passwordGenerator(length, uppercase, lowercase, numbers, symbol):
    upperchars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowerchars = "abcdefghijklmnopqrstuvwxyz"
    numberschar = "0123456789"
    symbolchars = " ~!@#$%^&*()_-+=[]|\:;<>,./? "

    allowedchars = ""
    password = ""

    if uppercase:
        allowedchars += upperchars
    if lowercase:
        allowedchars += lowerchars
    if numbers:
        allowedchars += numberschar
    if symbol:
        allowedchars += symbolchars

    for i in range(length):
        password += allowedchars[random.randint(0, len(allowedchars)-1)]

    return password

lengthOfPassword = int(input("Enter the length of your password: "))
uppercase = True
lowercase = True
numbers = True
symbol = True

new_password = passwordGenerator(lengthOfPassword, uppercase, lowercase, numbers, symbol)

print(f"The generated password is {new_password}")

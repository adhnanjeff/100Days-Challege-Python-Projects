from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

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

lengthOfPassword = 12
uppercase = True
lowercase = True
numbers = True
symbol = True

new_password = passwordGenerator(lengthOfPassword, uppercase, lowercase, numbers, symbol)


# ---------------------------- SAVE PASSWORD ------------------------------- #

def generatePassword():
    e3.clipboard_clear()
    e3.insert(0, new_password)

def getData():
    web = webe.get()
    mail = maile.get()
    passw = e3.get()
    with open("Base/Projects/Day 29/file1.txt", "a") as f:
        f.write(f"{web} | {mail} | {passw}\n")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.minsize(width=500, height=300)
window.title("Password Manager")
window.config(padx=20, pady=20)

c = Canvas(height=200, width=200)
logo_img = PhotoImage(file="Base/Projects/Day 29/logo.png")  # Check the path
c.create_image(100, 100, image=logo_img)
c.grid(row=0, column=1)

web = Label(text="Website:")
web.grid(row=1, column=0)
webe = Entry(width=35)
webe.grid(row=1, column=1, columnspan=2)

mail = Label(text="Email/Username:")
mail.grid(row=2, column=0)
maile = Entry(width=35)
maile.grid(row=2, column=1, columnspan=2)

passw = Label(text="Password:")
passw.grid(row=3, column=0)
e3 = Entry(width=21)
e3.grid(row=3, column=1)


gp = Button(text="Generate Password", width=14, command=generatePassword)
gp.grid(row=3, column=2)

add = Button(text="Add", width=36, command=getData)
add.grid(row=4, column=1, columnspan=2)  # Corrected columnspan value


window.mainloop()

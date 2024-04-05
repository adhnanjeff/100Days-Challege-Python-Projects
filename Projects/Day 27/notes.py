from tkinter import *

#Window Creation
#window = tkinter.Tk()
window = Tk()
#Window Size
window.minsize(width=500, height=300)
#Window Title
window.title("My first GUI Project")

#Label Creation

#my_label = tkinter.Label(text="I am a Label", font=("Monospace", 24))
my_label = Label(text="I am a Label", font=("Monospace", 24))

#Display the label 
my_label.pack()
"""      Multiple types of labelling
my_label.pack(side="bottom")
my_label.pack(side="left")
my_label.pack(side="right")
my_label.pack(side="top")
my_label.pack(expand=1)
my_label.pack(expand=0)
"""
#To change the text of the label
#my_label["text"] = "Hello"
my_label.config(text="Hello")

#Buttons

def buttonClicked():
    my_label.config(text="I got clicked") #Button on click changes the text
    l1.pack() #Button on click displays the label
    
"command" #Similar to onClick method in html, javascript
b1 = Button(text="ClickMe", command=buttonClicked)
l1 = Label(text="You clickde the button")
b1.pack()


#Entry

def button():
    ans = int(user_input.get())
    l2.pack()
    l2.config(text= ans)


user_input = Entry(text="Type")
user_input.pack()
b2 = Button(text="Display", command=button)
b2.pack()

l2 = Label()

#To have window to display
window.mainloop()
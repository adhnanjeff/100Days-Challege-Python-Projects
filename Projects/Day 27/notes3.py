#Tkinter form methods 

from tkinter import *

window = Tk()

window.minsize(width=500, height=600)
l1 = Label(text="This is a text Label")
l1.pack()

b1 = Button(text="Click Me")
b1.pack()

e1 = Entry()
e1.insert(END, "This is a sample text") #To have a string similar to placeholder
e1.pack()

t1 = Text(height=5, width=30)
t1.focus() #To make the cursor start in the textbox
t1.pack()

s1 = Spinbox(from_= 0, to_= 10)
s1.pack()

def scaleUsed(value):
    print(value)

sc = Scale(command=scaleUsed)
sc.pack()

def checkUsed():
    print(checkState.get())

checkState = IntVar()
cb = Checkbutton(text="Is on?", variable= checkState,command=checkUsed)
cb.pack()

r1 = Radiobutton(text="Is selected?")
r1.pack()

r2 = Radiobutton(text="Is selected?")
r2.pack()

def listbox_used(event):
    print(listb.get(listb.curselection()))

listb = Listbox(height=4)
fruits = ["apple", "orange", "grapes", "banana"]
for item in fruits:
    listb.insert(fruits.index(item), item)
listb.bind("<<ListboxSelect>>", listbox_used)
listb.pack()

window.mainloop()
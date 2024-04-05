from tkinter import *

window = Tk()
window.minsize(width=500, height=300)
window.title("Kilometer to Mile Converter")

def convert():
    km = float(e1.get())  # Convert input to float to handle decimal values
    mile = km * 0.621371
    l2.config(text=f"{mile:.2f} miles")  # Display result with 2 decimal places
    l2.grid(row=0, column=2)  # Corrected grid position for l2


l1 = Label(text="Kilometer")
l1.grid(row=0, column=0)

e1 = Entry()
e1.grid(row=0, column=1)

b1 = Button(text="Convert", command=convert)
b1.grid(row=1, column=0, columnspan=2)

l2 = Label(window)  

window.mainloop()

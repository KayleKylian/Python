from tkinter import *

root = Tk()

myLabel = Label(root, text="Hello World!")
myLabel2 = Label(root, text="My name is Jordan!")
myLabel3 = Label(root, text="How are you?")
myLabel4 = Label(root, text="Where are you from?")

myLabel.grid(row=0, column=0)
myLabel2.grid(row=1, column=0)
myLabel3.grid(row=2, column=1)
myLabel4.grid(row=3, column=1)

root.mainloop()

#Importing Module
from tkinter import *

#Creating root window
root = Tk()

#root window title and dimension
root.title("Welcome to GeekForGeeks")
#Set geometry (widthxheight) [Largura x Altura]
root.geometry('350x200')

#adding menu bar in root window
#new item in menu bar labelled as 'New'
#adding more items in the menu bar
menu = Menu(root)
item = Menu(menu)
item.add_command(label='New')
menu.add_cascade(label='File', menu=item)
root.config(menu=menu)

#Adding a label to the root window
lbl = Label(root, text = "Are you a Geek?")
lbl.grid()

#Adding Entry Field
txt = Entry(root, width=10)
txt.grid(column = 1, row = 0)

#function to display text
#when button is clicked
def clicked():

    res = "You wrote " + txt.get()
    lbl.configure(text = res)

#button widged with red color text inside
btn = Button(root, text = "Click me",
                     fg = "red", command=clicked)

#set Button grid
btn.grid(column=2, row=0)

#Execute Tkinter
root.mainloop()

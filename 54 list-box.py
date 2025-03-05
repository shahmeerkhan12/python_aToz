# lets work on list boxes in python
from tkinter import *

def submit():
   print(list.get(list.curselection()))

window = Tk()

# window.geometry('500x300')

label = Label(window,text=("Food List"), font=("arial",16),)

label.pack()

list = Listbox(window,bg="#ffffde",font=("arial",12),width=12)

list.pack()

list.insert(1,"pizza")
list.insert(2,"burger")
list.insert(3,"sandwich")
list.insert(4,"pasta")
list.insert(5,"bread")

list.config(height=list.size())

submit_button = Button(window,text="submit",command=submit)

submit_button.pack()

window.mainloop()
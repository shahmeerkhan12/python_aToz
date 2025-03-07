# lets work on list boxes in python
from tkinter import *

def submit():
   print(list.get(list.curselection()))

def add():
   list.insert(list.size(),entry_box.get())
   list.config(height=list.size())

def delete():
   list.delete(list.curselection()) # select and delete the item with cursor upon
   list.config(height=list.size()) # reset the size after deletion of item


window = Tk()

# window.geometry('500x300')

label = Label(window,text=("Food List"), font=("arial",16),)

label.pack()

list = Listbox(window,bg="#ffffde",font=("arial",14))

list.pack()

list.insert(1,"pizza")
list.insert(2,"burger")
list.insert(3,"sandwich")
list.insert(4,"pasta")
list.insert(5,"bread")

entry_box = Entry(window)
entry_box.pack()

submit_button = Button(window,text="submit",command=submit)
submit_button.pack()

add_button = Button(window , text="add_item",command=add)
add_button.pack()

delete = Button(window , text="delete_item",command=delete)
delete.pack()



window.mainloop()
from gc import disable
from tkinter import END, LEFT, RIGHT, Button, Tk, font, Entry
# entry widget:= accepts a single line of input from the user
window = Tk()
window.geometry('800x100')

def submit():
   username = entry.get()
   print('hello!' ,username)
   # lets say after submitting the name we want to disable the the buttons
   entry.config(state="disabled",bg="black",fg="blue")

def delete():
   entry.delete(0,END)

def backspace():
   entry.delete(len(entry.get())-1,END)
   
# label for singleline input
entry = Entry(window,
              font = ('arial',20),
              width=40,
              border=2,)
# some built-in methods

entry.insert(0,"heroshema-nagasaki")           
# if there is an entry for password then use this
# entry.config(show="#")
entry.pack(side=LEFT)


#label for submit button
submit_btn = Button(window,font=('arial',10),text="Submit",command=submit)
submit_btn.pack(side=RIGHT)

delete_btn = Button(window,font=('arial',10),text="Delete",command=delete)
delete_btn.pack(side=RIGHT)

backspace_btn = Button(window,font=('arial',10),text="Backspace",command=backspace)
backspace_btn.pack(side=RIGHT)

window.mainloop()
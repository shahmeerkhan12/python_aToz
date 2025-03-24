from tkinter import *

window = Tk()

def submit():
   input = text.get("1.0",END)
   print(input)

text=Text(window,bg="Light blue",font=("Ink free",20),fg="purple",height=10,width=20,padx=10,pady=10)
text.pack()

button = Button(window,text="submit",command=submit)
button.pack()

window.mainloop()
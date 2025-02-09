from tkinter import ACTIVE, DISABLED, Button, PhotoImage, Tk
from turtle import mainloop

def click():
   print("You click the button")

window = Tk()
buttonImage = PhotoImage(file="res_thumbsup.png")  

window.geometry("400x400")
button = Button(window,text=("click me"),bg="black",
                fg="white",pady=8,padx=4,
                font=("sans",10,"bold"),
                command=click,
                activebackground="white",
                activeforeground="black",
                state=ACTIVE,
                image=("res_thumbsup.png")
                ) # default active other include disabled and normal
button.pack()

window.mainloop()
from tkinter import Checkbutton, PhotoImage, Tk, IntVar, Image
from PIL import Image, ImageTk

window = Tk()

def display():
   if(x.get()==1):
      print("you agree!")
   else:
      print("you don't agree :)")
# instead you can use other variable types like string, boolean, etc
x = IntVar()

# home_icon = Image.open(r'C:\Users\Shamir Khan\py prog\phase 2\48 GUI\bird2.jpg')
icon = PhotoImage(file=r'C:\Users\Shamir Khan\py prog\phase 2\48 GUI\icon2.png')


check_btn = Checkbutton(window,
                        text=("I agree!"),
                        font=("arial",19),
                        variable=x,
                        onvalue= 1,
                        offvalue=0,
                        command=display,
                        bg="blue",
                        fg="green",
                        activebackground="blue",
                        activeforeground="green",
                        image=icon,
                        compound="left",
                        padx= 20,
                        pady= 20,
                        )

check_btn.pack()

window.mainloop()
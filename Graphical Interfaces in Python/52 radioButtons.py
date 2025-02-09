# radiobuttons:  are similar to checkboxes, you can only select one from a list/group
from operator import le
from tkinter import W, IntVar, PhotoImage, Tk, Radiobutton

# list for radio button labels
food = ['pizza','burger','sandwich']

# creating a window 
window = Tk()

# defining the var b/c so that each radionbutton has a seperate value
# IntVar() is an integer variable holder
x = IntVar()

icons = PhotoImage(file=r"C:\Users\Shamir Khan\py prog\phase 2\48 GUI\bird2.png")

for i in range(len(food)):
# creating a radiobutton and putting it on our window
   radiobutton = Radiobutton(window,
                             text=food[i],
                             variable=x,
                             value=i,
                             image=icons,
                             compound="left"
                          )
   radiobutton.pack(anchor=W)# anchor align the items


# showing the window 
window.mainloop()
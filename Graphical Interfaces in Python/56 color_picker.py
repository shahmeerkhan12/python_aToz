from tkinter import *
from tkinter import colorchooser

def click():
   # color = colorchooser.askcolor() # color is an array of two values (rgb_format, hex_format)
   # hexcolor = color[1]
   window.config(bg=colorchooser.askcolor()[1])


window = Tk()
window.geometry("399x233")
btn=Button(text="click me",command=click)
btn.pack()
window.mainloop()
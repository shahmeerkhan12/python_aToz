from tkinter import *
from tkinter import filedialog

def openFile():
   filePath = filedialog.askopenfilename(initialdir="C:\\Users\\Shamir Khan\\python_aToz\\Graphical Interfaces in Python",
                                         title="open file",
                                         filetypes=(("text files","*.txt"),
                                         ("all files","*.*")),
                                         )
   file = open(filePath,'r')
   print(file.read())

window = Tk()
button = Button(text="Open File",command=openFile)
button.pack()
window.mainloop()
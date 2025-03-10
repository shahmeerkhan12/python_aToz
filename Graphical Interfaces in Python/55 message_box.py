from tkinter import *
from tkinter import messagebox

def click():
   # we will display three different kinds of info Message_boxes
   # 1
   # messagebox.showinfo(title='This is message Box TITLE', message="Hey! you can proceed")
   # 2
   # messagebox.showwarning(title='This is message Box TITLE', message="Security Warning!")
   # 3
   # messagebox.showerror(title='This is message Box TITLE', message="There occured an Error!")
   # 4
   # if messagebox.askokcancel(title="AskOkCancel",message="Start the Quiz?"):
   #    print("You are ready for test!")
   # else : print("You are not ready for test!")
   # 5
   # if messagebox.askretrycancel(title="askretrycancel",message="Retry the Quiz?"):
   #    print("Lets start again the test!")
   # else : print("You are not ready for test!")
   # 6
   # if messagebox.askyesno(title="askyesno",message="do you like cake?"):
   #    print("Lets eat the cake")
   # else: 
   #    print("You don't like the cake")
   # 8
   answer = messagebox.askquestion(title="askquestion",message="Did you visited UK?")
   if(answer=="yes"):
      print("he visited UK")
   else: 
      print("He didn't visited UK")

window= Tk()  

click_btn = Button(text="click me",font=('Helvitica',12,'bold'),command=click)
click_btn.pack()


window.mainloop()
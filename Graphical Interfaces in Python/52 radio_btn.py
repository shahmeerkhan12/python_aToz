from tkinter import W, Checkbutton, PhotoImage, Radiobutton, Tk, IntVar, Image
from turtle import position
from PIL import Image, ImageTk
 
food = ['piazza','biryani','pasta']
window = Tk()

x = IntVar()

def order():
      if(x.get()==0):
        print('you like:', food[0])
      elif(x.get()==1):
         print('you like:', food[1])
      elif(x.get()==2):
         print('you like:', food[2])
      else:
         print('OK!')
 
# instead you can use other variable types like string, boolean, etc

# home_icon = Image.open(r'C:\Users\Shamir Khan\py prog\phase 2\48 GUI\bird2.jpg')
icon = PhotoImage(file=r'C:\Users\Shamir Khan\py prog\phase 2\48 GUI\icon2.png')

for index in range(len(food)):
   radio_button = Radiobutton(window,
                        text=food[index],
                        font=("arial",19),
                        variable=x,
                        value= index,
                        command=order,
                        image=icon,
                        compound="left",
                        padx= 20,
                        pady= 20,
                        
                        )
   radio_button.pack(
      anchor=W
   )


window.mainloop()
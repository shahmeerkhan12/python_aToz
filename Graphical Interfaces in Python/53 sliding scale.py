from tkinter import *

def submit():
   print("The Temperature is: " + str(scale.get()) + "degrees C")

window = Tk()


scale = Scale(window,
              from_=900,
              to=0,
              length=400,orient=VERTICAL,
              font=("consolas",10),
              tickinterval=10,
              troughcolor='#a4c4c4',
              fg='black',
              bg='silver'
            

              )
scale.set(50) # suppose your scale range changes by huge numbers and u always the scale is on the 
# middle by default then use this
scale.set(((scale['from']-scale['to'])/2)+scale['to'])
scale.pack()

button = Button(text="submit", command=submit)
button.pack()

window.mainloop()
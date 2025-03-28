# widget : gui elements like buttons, lables, images, text boxes, etc 
# windows : a container to hold the widgets

from tkinter import *
from PIL import Image, ImageTk

window = Tk() # instantiate the windows object

window.geometry("600x400")
#adding the title to the window
window.title("Python GUI Creation")
# it is necessary to provide the full path, even if the image file is located in the same directory 
# adding the icon to the title bar
icon = PhotoImage(file="Graphical Interfaces in Python\\burger.png")
window.iconphoto(True,icon)
# photo_image = tk.PhotoImage(file=path_to_image)


# creating Labels

# logo_image = Image.open(r'C:\\Users\\Shamir Khan\\py prog\\phase 2\\48 GUI\\awkum.jpg') #this step is optional
photo_image = PhotoImage("awkum.jpg")

label = Label(window,text="Welcome to Python",
              font=('Arial',20,'bold'),
              bg='lightblue',
              relief='raised',
              border=10,
              padx=20,
              pady=30,
         #how can we an image to the label
         # remember for below statement i have ignored the typeCheck  type: ignore
              image=photo_image, # this is so much important, provide the variable inWhich your stored the image # type: ignore
              compound='bottom'
              )
label.pack()#places the label at the default center position
# label.place(x=50,y=0)#places the label at the defined position position
label_2=Label(window,text="Creating and Adding new widget elements in Python is awesome and very simple.",
              font=('serif',15,'italic'),
              padx=20,pady=30,border=10,borderwidth=10,relief=RAISED,justify="right",underline=0)
label_2.pack()
# 3rd label
label_3 = Label(window,text="Abdul Wali Khan University Mardan\nawkum@edu.pk.com",
              font=('Arial',20,'bold'),
              bg='lightblue',
              relief='raised',
              border=10,
              padx=20,
              pady=30,
         #how can we an image to the label
         # remember for below statement i have ignored the typeCheck  type: ignore
              image=photo_image, # this is so much important, provide the variable inWhich your stored the image # type: ignore
              compound='bottom'
              )
label_3.pack()
# 3rd label ended
window.mainloop() # places a window on computer screen and also listen to events(advance concept)

# in this program we well pass an obje as parameter

class Car:
   
   color = None
   def car_color(self): # accepts two param 1 is object of type Car and 2 is string color
      print("Mercedes   1996MRDS_B \nColor Blue")  

def change_Color(car,color): # accepts two param 1 is object of type Car and 2 is string color

   car.color= color

# lets create some objs

car1=Car()

#lets change the color of objs using the change_color function

change_Color(car1,"blue")

print(car1.car_color())

# we can add further class and use the same method to do so or other needed

#next tutorial Duck typing


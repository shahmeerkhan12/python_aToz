#super() = function that gives access to the methods of the parent class
#          returns a temp object of the parent class when used


class Rectangle :
   def __init__(self,length, width):
      self.length=length
      self.width=width

class Square(Rectangle) :
   def __init__(self, length, width):
      super().__init__(length, width) #super function

   def area(self):
      return self.length*self.width 
   
class Cube(Rectangle):
   def __init__(self, length, width,height):
      super().__init__(length, width)
      self.height=height

   def volume(self) :
      return self.length*self.width*self.height
   
lenth=int(input("enter length: "))
width=int(input("enter width: "))
height=int(input("enter height: "))

square=Square(lenth, width)
volume=Cube(lenth,width,height)

print("the area of square is:",square.area()," squareMeter")
print("the volume of cube is:",volume.volume()," cubicMeter")
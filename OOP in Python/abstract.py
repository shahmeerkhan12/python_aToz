# abstract class = a class with one or more obstract methods
# abstract method = a methods that has a declaration but no implementation
# abstract class prevents the user from creating the objects of that class
# abstract methods compels the child class to override these method

from abc import ABC, abstractmethod

class Vechile(ABC):
   @abstractmethod
   def go(self): #declared not implemented
      pass

class Car(Vechile):
   def go(self):
      print("Car can go!")

class Motorcylce(Vechile):
   def go(self):
      print("MotorCycle can go!")


car = Car()
motorcylcle = Motorcylce()

car.go()
motorcylcle.go()
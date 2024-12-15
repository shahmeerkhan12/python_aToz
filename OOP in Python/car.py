class Car:
   car_wheels = 4 # class variables usually declared and initialized outside of the constructor

   def __init__(self,name,model,color,manufacture): 
      self.name = name # instance variables always declared inside of the constructor
      self.model=model # instance variables
      self.color = color # instance variables
      self.manufacture = manufacture # instance variables


   def drive(self): #self is the parameter and is the object that will use this method for
      print("this "+self.model+" can drive")
      return self

   def start(self):
      print("this "+self.model+" can start")
      return self      

class Sports:
   sports = "more than 200"
   # use some default values for parameters
   def __init__(self,s1='football',s2='baseball') :
      self.s1=s1
      self.s2=s2

   def famousSport(self):
      print(self.s1," is a famous sport")
      return self















      # next tutorial inheritance in python

      
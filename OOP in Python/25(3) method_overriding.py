class Animal:
   def eat(self):
      print("This animal is eating.")
   
class Rabbit(Animal):
   def eat(self): # overriding the eat method of the animal class
      print("This rabbit is eating bread.")

rabbit= Rabbit()
rabbit.eat()

#next tutorial Method Chaining
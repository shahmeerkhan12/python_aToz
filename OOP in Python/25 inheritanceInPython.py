# multilevel inheritance in python
# when a class is derived from a class that is itself derived from another one is called as multilevel inheritance

class Organisims:
   
   def have_cells(self):
      print("All organisims has cells.")

class Animal(Organisims) :
   def eat(self):
      print("All animals eat.")

class horse(Animal):
   def run(self):
      print("All horses are animals.")

# check whether horse class can inherit various properties from the it parent classes
My_horse=horse()
My_horse.run()
My_horse.eat()
My_horse.have_cells()

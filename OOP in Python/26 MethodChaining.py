class Organisims:
   
   def have_cells(self):
      print("All organisims has cells.")
      return self
   def eat(self):
      print("All animals eat.")
      return self
   def feel(self):
      print("All animals can feel.")
      return self
#method chaining is the technique in which the objects calls all or a few methods in a single line sequentially
      
animal = Organisims()
# method chaining
animal.have_cells().eat().feel() 

# let if we have more methods then we can do the following

animal.\
         have_cells().\
         eat().\
         feel()

#  next tutorial
 # super() function

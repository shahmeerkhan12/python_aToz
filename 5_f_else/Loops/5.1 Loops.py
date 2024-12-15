# while-loop
print("while-loop")
name = ""
while len(name)==0 :# as long as the name string_var is empty, it will keep asking for name
    name=(input("Please input your name "))
print("Hello! "+ name)# prints the name

print("*******************************")

#  second method
# works the same as above

name = None
while not name :
    name=(input("Please input your father name: "))
print("Welcome "+ name)

print("*******************************")

# for loop 
# syntax: for i in range(starting_point,ending_point,step)

for i in range(0,6,2):
   pass

# will iterate through the string 'shahmir khan'
print("ForLoop: ")
for i in "shahmir khan":
   print(i,end=" ") # prints all the string elements in the string 

print()
print("*******************************")



# range shows the limit to iterate over

for i in range(10+1) :
   print(i, end = " ")
print()

print("*******************************")

# # to iterate over a string we use the following method

for i in "Shahmir khan" :
   if i=='m':
      pass # pass/continue are loop control statements
   else:
      print(i,end=" ")

print()

print("*******************************")

for i in "Shahmir khan" :
   if i=='m':
      break # pass is a loop control statement
   else:
      print(i,end=" ")  
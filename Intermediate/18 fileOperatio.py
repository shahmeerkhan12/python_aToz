# file operations in python:
# we will use the python 'os' and 'shuttle' libraries for file operations and manipulation

import os

# before writing or reading from a file, First:
# let we check whether a file\location exist in our computer

path = "C:\\Users\\Shamir Khan\\PYTHON PROJECTS LOCAL"

if (os.path.exists(path)) :
   print("The Location exist!") 
   if os.path.isfile(path) :  
      print("That is a file")
   elif os.path.isdir(path) :
      print("That is a directory")
else:
   print("the location doesn't exists!")

print('___________________________________')

# lets read from a file

print('Reading the file')
print('___________________________________')

# when the file and the program are in the same directory

with open('text.txt') as file: 
   print(file.read())

# now what if the FILE is in some other LOCATION/DIR, just copy the FILE LOCATION

print('___________________________________')

# it is often a good practice to include the try, except statements:

try :
      with open("C:\\Users\\Shamir Khan\\PYTHON PROJECTS LOCAL\\1test.txt") as file :
         print(file.read())
except FileNotFoundError :
    print("That file was not found :")
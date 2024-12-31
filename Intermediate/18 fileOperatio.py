import os


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

   # lets read from a file
print()
print('Reading the file')

# when the file and the program are in the same directory

# with open('test.txt') as file: 
#    print(file.read())

# now the file is in some other location, just copy the file location
# with open("C:\\Users\\Shamir Khan\\Videos\\hello.txt") as file :
#       print(file.read())

# if a file does not exist then do the follwing

try :
      with open("C:\\Users\\Shamir Khan\\PYTHON PROJECTS LOCAL\\1tes t.txt") as file :
         print(file.read())
except FileNotFoundError :
    print("That file was not found :")
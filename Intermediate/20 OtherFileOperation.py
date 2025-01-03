#copyfile()=copies contents of a file
#copy()=copyfile() + permission mode + destination can be a directory
#copy2() = copies + copies metaData(file creation and modificatoin data)
 
# assume that both files are in the current folder

import shutil
#remember the first parameter acts as the source and the second is destination
shutil.copy2('test.txt','MyTextfile.txt')

# tut 21 move file

import os

source = "MyTextFile.txt"
# for testing purpose only
destination= "C:\\Users\\Shamir Khan\\copi\\MyTextFile.txt"
 
try:
    if os.path.exists(destination) :
        print("The file already exists!")
    else:
       os.replace(source,destination)
       print(source+ "was moved")
except FileNotFoundError:
    print(source+"File not found")




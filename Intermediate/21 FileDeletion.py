import os

import shutil
# from shutil import rmtree
# shutil.rmtree('empty folder')
source = "empty"
# remember that the remove function cannot remove empty folders intead use
# os.removedirs('folderr')
# if a folder contains files and other folders then these function cannot work instead u will use the
# import shutil, library and then use the module shutil.rmtree(path)

try:
      # os.remove(source) # removes files
      os.removedirs(source) # removes empty dir
     # shutil.rmtree(path) # removes dir that contains files and other folders.
except FileNotFoundError:
   print("*****************")
   print( "File not Found!")
   print("*****************")
   #new folders are not removedff

except PermissionError:
   print("*****************")
   print("You donot have the access to delete this folder.")
   print("*****************")

else:
   print("_________________________")
   print("File Removed Successfully")
   print("_________________________")
# **kwargs:    this technique is the same as the *args technique but here instead the function will be able to 
#              accept varying amount of keyword args and it uses a dictionary to pack those parameters

def Hello( **kwargs) :#remember that ** part is necessary the name kwargs can be any other name like names etc
   
   print("Hello", end=" ") # simple Hello word with an empty space after
  
   for key,value in kwargs.items() : # as dict stores data in key:value pairs so.......
      print(key,": ",value,end=" ")

#pass as much as keyword arguments as you need 
 
Hello(Title="Mr.",first="Ali",middle="Muhammad",last="Khan")

print ()

Hello(Title="Mr.",first="Ghulam")
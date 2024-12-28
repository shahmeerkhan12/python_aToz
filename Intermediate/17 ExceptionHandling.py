# Exception handling in python
# consists of a :=
#                 try: 
#                 except: 
#                 else: 
#                 finally:

try :
   numerator=int(input("please input a number to be divided: "))
   denumerator=int(input("please input a divisor: "))
   result=numerator/denumerator

except ZeroDivisionError as e:
   print(e)
   # print("You cannot divide by Zero!")

except ValueError as e:
   print(e)
   print("Please input only integer")
   
except Exception as e:
   print(e)
   print("Something went wrong:(")

else:
   print((result))

# there is also a finally block as shown below, which always execut for the purpos in a program if you 
# open some files, then the finally block is used to close these files

finally:
   print("It Always Happens")


# local: access inside function only
# global: acess outside and inside functions

# python follow rule

# L=local, E=enclosed, G=global, B=built-in

# global scope
name_1="bro" 

def localScope() :
   name_1="code" # local varible
   print("inside function: ",name_1)

# call the localScope()
localScope()

# simply checkout does the local var is accesible outside the function! NO
print("Outside function: ",name_1)
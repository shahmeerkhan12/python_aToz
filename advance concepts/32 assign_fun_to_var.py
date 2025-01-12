# assigning functions to variables is a technique in python 
# demonstrated in the following way:

# lets i a function
def disp_hello():
   print("Hello Mannn!")
print()
hello=disp_hello # assigns the adress of the disp_hello function to the "hello" variable
print(hello)     # prints the adress at of disp_hello function variabel
print(disp_hello)#print the same mem_adress as above
print()
# other examples

# i will assign the built in print function adress to a variable:

my_print_fun = print
my_print_fun("It is working as if it is a real built-in print function.")

# print()

my_print_fun(my_print_fun)
# AND 
my_print_fun(print())
# # will always print the same mem-address as these both refers to the same location
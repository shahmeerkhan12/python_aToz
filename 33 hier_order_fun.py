# higher order functions: a higher order fun is one tht could either:
#                                      1:  accept a function or
#                                      2:  return a function

#example 1:
print()
def upper(text):
   return text.upper()
def lower(text):
   return text.lower()

# higher order fun

def change_case(func):
   text=func("The storm took over the North Korea.")
   print(text)

change_case(upper)

# example 2

def divisor(x):
   def dividend(y):
      return y/x
   return dividend
#first pass a value to the divisor function and store it in variable, lets say 'divide'
divide = divisor(10) 
#then make a call to the inner function by passing the a value to it
print(divide(1000))


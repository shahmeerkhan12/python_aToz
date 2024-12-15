#reduce() :=  by applying a function, reduce method can return a single cumulative value,
#             a function should be performed on the first two elements and it is repeated for the 
#             remaining elements until a single value remains

import functools

# EXAMPLE 01
spaced_letters = ["D","U","B","A","I"]
# u can define funciton outside, and then pass into the method
# or write inline as lambda function directly
word = functools.reduce((lambda x,y,:x+y),spaced_letters)
print(word)

# EXAMPLE 02
product = [1,2,3,4,5,6]
factorial = functools.reduce((lambda x,y,:x*y),product)
print(factorial)
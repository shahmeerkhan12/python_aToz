# map() :=> map function applies to iterables (list, tuples,etc)
# map(function, iterables): takes two parametres. one is function that you want to apply to
# iterable and the second is the iterable (list, tuple) to which the function must applied
# Example:
# suppose a list with items and their prices in USDollars, but we want to convert the price into euros:
from math import floor


store = [
   ("shirt",20),
   ("sweater",10),
   ("jeans",30),
   ("hat",14)
]
# since one dollar is 0.80 euros
# using the lambda functon
# floor function is used to roundup the number
# to select prices from the store list then
# method 01
# this function will not only convert the currency but also holds the other items like the shirts_names
# from the list by the "price[0]" statement. while price[1] refers to the prices in dollars
to_euros = lambda price:(price[0],floor((price[1]*0.80)))

# now is the use of map function
# create a new variable, another thing that the original list remain the same.

store_euros = map(to_euros,store)

for i in store_euros:
   print(i)
#  *args:   Techinique by which parameters will pack into a 'tuple' so that a function 
#           can accept varying amount of arguments


# let show it by a   function add()

def add(num1,num2) :
   sum=num1+num2
   return sum

#print(add(90,90))   # if i want to add more than two numbers then what should i do:

# *args

from ast import arg

def add(*args) :
  #args[0]=89 #like tuple is unchangeable(shows error)

  numbers=list(args) # args converted into a list

  #  variable to hold the sum
  sum=0 
  # run loop thru list 'numbers'
  for i in numbers :
      sum+=i
  # return  the sum of the list 'numbers'
  return sum

# call it and print the returned number
print(add(120,90,40,50,80))




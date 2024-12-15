#  *args: Techinique, let show it by a function add()
# parameters will pack into a tuple so that a function can accept varying amount of arguments

# def add(num1,num2) :
#    sum=num1+num2
#    return sum

#print(add(90,90))   # if i want to add more than two numbers then what should i do:

# *args

from ast import arg


def add(*args) :
  #args[0]=89 #like tuple is unchangeable(shows error)
  args=list(args) # cast into a list
 
  args[0]=0  #and it will work now
  sum=0
  for i in args :
      sum+=i
  return sum

print(add(120,90,40,50,80))




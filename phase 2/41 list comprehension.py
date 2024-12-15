# list comprehension = a way to create new list with less syntax,
#                       it can mimic certain lambda funcitons, easier to read
# syntax :=          list = [expression for item in iterable]

# traditional approach
squares  = []
for i in range(1,11):
   squares.append(i*i)
# print(squares)

# method 02(list comprehension)

# squares2 = [i*i for i in range(1,11)]
# print(squares2)

# example 2

# traditional method 

# a list of student marks
result = ["90","67","76","88","39","40","50"]
# let us filter the list for stdents who have passed the exam
passed =list(filter(lambda x: x>="60",result))
print(passed)

# more advanced(adding conditions to the list comprehension)

# list comprehension method
# we are adding an extra parameter(statement) to the syntax for list comprehension
# syntax:= list = [expression for item in iterable conditions(if any)]

passed= [i for i in result if i>="60"]
print(passed)

# 03 we can also add the if/else conditions as well
# now if want to replace the marks lower than 60 another value "failed"
# the syntax now will be: list = [expression if/else for item in iterable]
passed = [i if (int(i))>=60 else "Failed" for i in result]
print(passed)
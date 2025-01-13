# sort method:can only be used for list:
# sort method is a builtin method for lists only.
# sort function: used for iterables, this method donot modify the original list or tuple:
# sort method is used for all kind of iterables

# part 1 sort() method
# List
student= ["Yaseen","Abdullah","Ibrar Ali","Muhammad Anas","Zakariya"]
# print(student[2])
student.sort(reverse=True) # to print in descending order
for i in student:
   print(i)
# print(student[2])

# the sort() function
# tuple
FoodItems= ("Chicken","Beep","Mutton","Biryani","Kabli Pulao")
# we will use the sort function for tuples
sorted_FoodItems = sorted(FoodItems, reverse=True)
# we can see the original tuple is not changed
# we can descend the array by the following
# sorted_students = sorted(student,reverse = True)
print("_________________________")
for i in sorted_FoodItems:
   print(i)
print("_________________________")

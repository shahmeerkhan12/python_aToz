# map(function_to_bePerformed, iterable_overWhichTheFunctionIsToBePerformed)
students = [
   ("Lisa. Miller",""),
   ("JP. Morgan"," ")
   ]

# def add(students):
#    for i in students:
#       print(i, " registered")

mod = lambda students: print(students[0]," registered")

reg_students= map(mod,students)

for i in reg_students:
   print(i)
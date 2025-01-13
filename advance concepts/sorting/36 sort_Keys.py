# now we will use the sort method in complex tasks:
# suppose that we have a 2D list

student = [("Asad","A",19),
           ("Natasha","C",20),
           ("Kamran","B",21),
           ("Moez","E",23),
           ("Bell","D",24)]
# the default sort method, that is sorting by the Names colum in the 2D list
# student.sort()
# for i in student:
#     print(i)

print('------------------------')

# but i want to sort by grades rather than name
# we can see that the grade in tuple is the second column

def sortByGrade():
    grade = lambda grades: grades[1]
    student.sort(key=grade)
    for i in student:
        print(i)  
  
print('------------------------')

# let if i want to sort by age, that is youngest to eldest
def sortByAge():
    by_age = lambda age : age[2]
    student.sort(key=by_age)
    for i in student:
        print(i)

while True:
    sort_by= None
    sort_by=input("How do you want to sort the List(student):(age/grade)").lower()
    if(sort_by=='age'):
        sortByAge()
    elif(sort_by=='grade'):
        sortByGrade()
    else:
        break

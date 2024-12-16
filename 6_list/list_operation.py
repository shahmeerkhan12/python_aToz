# to deomonstrate list data type/data structure

sports = ["Football","Hockey","Cricket","Volleyball"]
evens = [2,4,6,8,10,12,14]
grades = ['A','B','C','D','F']

print() # to print an extra line

# print(sports)

#to print a paricular element in the list

# print(sports[2],sports[3])

#to insert another element at any index
sports[1]="Racing"
sports.append("Rugbey")
# various function assocaited with a list

sports.append("Rugbey")
sports.insert(0,"Futsal")
sports.append("Atheletics")
sports.append("Boxing")
# sports.pop() #removes last element
# sports.remove("Football") #romoves the value
# sports.sort()
# sports.reverse()
# sports.clear()

#printing each element in the list by for loop

for a in sports :
   print(a,end=" ")
print()


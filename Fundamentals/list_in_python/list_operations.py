# performing some useful operations on lists

sports = ["Football","Hockey","Cricket","Volleyball"]

# adding new elements
sports[1]="Rugbey"

# adding element to the end of the list
sports.append("Running")

# some more built-in methods on list

sports.pop() # removes the last element

sports.remove("Football") #removes the value

sports.sort() # will sort the list in ascending order

# if you want to sort in descending order then use following

sports.sort(reverse=True)

sports.reverse() # reverses the array

sports.clear() # REMOVES all the list elements


#printing each element in the list by for loop

for a in sports :
   print(a,end=" ")
print()

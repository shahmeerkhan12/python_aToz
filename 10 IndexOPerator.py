# index operator [] = works to access a given index/element of a string list or tuple

name = "harry poter"

#if (name[0].islower()) :
   #name=name.capitalize()

# now let make substrings

First_name=name[0:5].upper() 
first_name=name[:5] #remember if yr substring starts with 0 you can omit 0 in the index
print(First_name)
print(first_name)

Last_name=name[6:]
print(Last_name)

# what if i want to access the last character of the string

Last_Char = name[-1] # as indexing from the opposite side starts with -1 so the last element is at index -1

print(Last_Char)
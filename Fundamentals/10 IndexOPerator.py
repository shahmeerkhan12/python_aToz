# index operator [] = works to access a given index/element of a string list or tuple

name = "harry poter"

# capitalize the first character of the name 
if (name[0].islower()) :
   name=name.capitalize()

# now let make substrings

# strings first 5 characters
First_name=name[0:5].upper() 

first_name=name[:5] #remember if substring starts with 0 you can omit 0 in the index

# print(First_name) # prints the substring harry but capitalized
# print(first_name)  # prints the substring harry

# will print the last name, start=6 and stop=end of original string
Last_name=name[6:]
print(Last_name)

# what if i want to access the last character of the string

# as indexing from the opposite side starts with -1 so the last element is at index -1
Last_Char = name[-1] 

# print(Last_Char)
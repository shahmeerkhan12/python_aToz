# SET? a set is an unordered, unindexed collection of data, it also have no duplicates
# if you included any duplicate value the set will treat it as a single vlaue, i.e. ignores repeated values
utensils = {"fork","spoon","knife","lunch Box"}
dishes = {"plate","hotpot","cup","lunch Box"}

utensils.add("napkin")
utensils.remove("napkin")
#utensils.update(dishes) #adds the whole another set to the utensils set
# utensils.clear() 
print()
print(utensils.difference(dishes))
print()
print(utensils.intersection(dishes)) #prints the common item in these two sets
print()
print(utensils.union(dishes))
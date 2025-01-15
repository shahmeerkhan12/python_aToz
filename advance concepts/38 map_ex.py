# an example on map() function:
#let we have a list 
employee = [
   ("Asad Khan",23,150000),
   ("Mubashir Zaid",24,200000),
   ("Khaleeq Jafar",25,170000)
]
# let I want to add the prefix Mr. to each of the name in list then
# define a function to add the prefix

update_emp = lambda newEmployee:("Mr. "+newEmployee[0],newEmployee[1],newEmployee[2]*(120/100))

# def update_emp(employee):
#    return ("Mr. "+employee[0],employee[1])

new_employee = map(update_emp,employee)

for i in new_employee:
   print(i)

# In short map function is a great tool that u can use to 
# change and modify existing list without changing the original 
# list/list elements
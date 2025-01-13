# lambda fun: used to perform so comman, basic tasks like addition, mult, div, strings_concatenation, etc;
# syntax: 
#           lambda_keyword parameters : expression




# part 01*************
# normal function
def add(num1, num2):
   return num1+num2
#print(add(12,20))

#lamnda function
sum=lambda num1,num2:num1+num2
mult =lambda num1,num2:num1*num2
div =lambda num1,num2:num1/num2
# print((div(212,32)))

# part 02 ***************
# name = lambda first_name, last_name:first_name+" "+last_name
# print(name("Roger","Pressman"))
# age_check = lambda age:True if (age>18) else False
# print(age_check(19))

# part 03 ***************
def verify(f_name,l_name,age,country):
   print("\nName: ",f_name," ",l_name)
   print("Age: ",age,)
   print("Country: ",country,"\n")
   age_check = lambda age:True if (age>18) else False
   if age_check(age):
      region = lambda country: True if (country!="North Korea") else False
      if region:
         print("Verification successful!\nYou can join the community now.")
      else:
         print("You are not allowed to join the community.")

verify("shahmir","khan",20,"Pakistan")
verify("shahmir","khan",20,"North Korea")
verify("Zaid","Ali",22,"England")
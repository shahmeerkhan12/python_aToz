# checking conditions through if_else

age = int(input("how old are you?   ")) # input is converted into number
if (age) >= 20 :
    print("You are eligible")
elif age<=18 :
    print("you are not eligible")
else :
    print("incorrect input")       
 
# temp shows temperature

temp = int(40)
 # here two conditions are checked 'and' operator helps to check two or more conditions
if temp>=0 and temp<=30:
    print("You can go outside")
elif temp>30 and temp<50:
    print("The temperature is very high and you cannot go outside")
else:
    print("plese input a valid number")














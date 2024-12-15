
#def Welcome():#function with no parameters
 #  name = input("please input your name: ")

  # by default the age input is taken as a str input
  # age=input("please input your age: ") 
   #Hello_user(name,age)

 #function with parameter "user"

#def Hello_user(user,age):
 #  print("Hello! " +user+", You are " + age + " years old")

# iam converting the str input "age " into integer type by casting
  # if (18<=int(age)<=40) : 
   #   print("You're elegible for the post. Thank you.")

# Call to functions
#Welcome()

#functions and retrurn statements

def mulitply(num1, num2) :
   return (num1*num2)

number1=3
number2=4
# a call to mulitiply function
print("product of: ", number1," * " , number2," =", + mulitply(number1,number2))
print("prodcut of ",+number1," and ",number2," is ",mulitply(number1,number2))

# key word arguments
# arguments preceded by identifier when we pass them to a function, order does not matter

def Hello(first,middle,last) :
   print("Hello"+" "+first+" "+middle+" "+last)

print(Hello(last="khan",middle="ali",first="Asad"))
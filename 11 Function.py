# function := is a set of statements that performs specific defined by users or built-in to the language

# python functions :=  syntax

# def function_name ( arguments ): 
#    function_body

# function with no parameters
name="Shahmir Khan"
def Welcome():
  print("Welcome to Python: ",name)

# lets call the Welcome()
Welcome()

# function with parameters
def Hello_user(user,age):
  print("Hello! " +user+", You are " + age + " years old")

#   by default the age input is taken as a str input

age=input("please input your age: ") 
Hello_user(name,age)

# functions with retrurn statements

def mulitply(num1, num2) :
   return (num1*num2)

number1=3
number2=4

# a call to mulitiply function

print("product of: ", number1," * " , number2," =", + mulitply(number1,number2))
print("prodcut of ",+number1," and ",number2," is ",mulitply(number1,number2))


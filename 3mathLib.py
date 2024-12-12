import math

# 01:=  ceil() function to roundup the given number to the nearest  (exclude the decimal part)
pi = 3.14
# OR
pi_value = math.pi
# printing the original value
print(pi_value)
# printing the roundup value 
print(math.ceil(pi))

# 02 : abs(number) := will the absolute value of the given number
neg = -33
print(abs(neg))   

# 03 : round(number) := will give the rounded value
# if number is like 2.5, its rounded value is 3
# if number is like 2.8 (decimal part is .5 or greater) output will be its nearest upper number
print("rounded number: ",round(pi))

# returns the nearest lower number (3 in this case is ouput)
print("floor value: ",math.floor(pi))

print(int(math.sqrt(99))) # just to get the exact integer value
# print(pow(pi,2))  #take the power

# 04 min and max functions
num1=1
num2=2
num3=3

#return the minimum number of prvided number
print(min(num1,num2,num3))

#return the maximum 
print(max(num3,num2,num1)) 
# #     str.format( )     := this is an amazing function can be applied to strings

# case 1: 

text="The {} jumped over the {}"
print(text.format("cow","moon"))

# case 2

animal='cow'
thing='moon'

# the single line statement to accompleish the task
print("The {} jumped over the {}".format(animal,thing))

# OR

# # # use positional arguments
print("The {1} jumped over the {0}".format(animal,thing))

# case 3

name = "Abdullah"
print("Hello {}".format(name))

# # let add some padding and then print another statement

# # you can use > or < sign to right and left align

print("You are welcome, Mr.{:<10}.".format(name)+" Nice to meet you. left justified")

print("You are welcome, Mr.{:>20}.".format(name)+" Nice to meet you. right justified")

print("You are welcome, Mr.{:^10}.".format(name)+" Nice to meet you. mid justified")



#formating numbers

number=3.14159

# .4f indicates that the pi number must have 4 digits after the decimal
print("the number pi is: {:.4f}".format(number))

# putting a coma after a thousand

num=100000

print("The number with comma after thousands unit: {:,}".format(num))

# # number conversions

inDecimal=1000
# to binary
print("The binary of ",str(inDecimal)+"  is: {:b}".format(inDecimal))
# to ocatal
print("The octal of ",str(inDecimal)+"  is: {:o}".format(inDecimal))
# to hexadecimal
print("HexDecimal : ",str(inDecimal)+"  is: {:X}".format(inDecimal))
# to scientific notation
print("Scientific : ",str(inDecimal)+"  is: {:e}".format(inDecimal))


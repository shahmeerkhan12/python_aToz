# #     str.format()
# # text="The {} jumped over the {}"
# # print(text.format("cow","moon"))

# # animal='cow'
# # thing='moon'

# #the single line statement to accompleish the task
# # print("The {} jumped over the {}".format(animal,thing))

# # # use positional arguments
# # print("The {1} jumped over the {0}".format(animal,thing))


# # padding and other formating tools



# name = "Abdullah"
# print("Hello {}".format(name))

# # let add some padding and then print another statement
# # you can use > or < sign to right and left align
# print("You are welcome, Mr.{:<10}.".format(name)+" Nice to meet you. left justified")
# print("You are welcome, Mr.{:>30}.".format(name)+" Nice to meet you. right justified")
# print("You are welcome, Mr.{:^10}.".format(name)+" Nice to meet you. mid justified")



# #formating numbers
# number=3.14159
# print("the number pi is: {:.2f}".format(number))

# # coma after a thousand
# num=100000
# print("The number with comma after thousands unit: {:,}".format(num))

# # binary of a number
inDecimal=1000
print("The binary of ",str(inDecimal)+"  is: {:b}".format(inDecimal))
print("The binary of ",str(inDecimal)+"  is: {:o}".format(inDecimal))
# print("HexDecimal : ",str(inDecimal)+"  is: {:X}".format(inDecimal))
# print("Scientific : ",str(inDecimal)+"  is: {:e}".format(inDecimal))
fillBlank = "The sun rises in the East. (true or false) {}"
choice=input()
print(fillBlank.format(choice)
)
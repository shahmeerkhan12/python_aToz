import random

# will generate a random number between 9 and 90
x=random.randint(9,90)
print(x)

 # printing the floating p  oint numbers, range is 0 to 1
y=random.random()
print(y)

# the rock paper and scissors
mylist=['rock','paper','scissor']

# will pick a random choice each time the program runs from the list 
z=random.choice(mylist)

print(z)

# # lets shuffle, 

cards=[1,2,3,4,5,6,7,8,9,"J","Q","k","A"]

# we shuffle the cards like this
random.shuffle(cards)

# every time a random sequence will be printed to the console
print(cards)

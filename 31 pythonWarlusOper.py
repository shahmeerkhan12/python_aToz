#python 3.8 update: warlus operator :=
# as assignment operator that is a part of a larger expression
# a warlus operator works by assigning values to variables in a larger expression.
# lets see how does it work:

# exple#1
happy = True
print( happy) # it will print true but if we want to write it within a single line using the warlus operator: then

print( happy := True )

# example # 2

# foods = list()
# while True:
#    food= input ("what is your favourite food: ")
#    if food == 'quit':
#       break
#    foods.append(food)

# now i will wrap the whole upper in to fewer lines using warlus opeartor
foods = list()
while food := input("what is ur favourite food: ") != "quit":
   foods.append(food)
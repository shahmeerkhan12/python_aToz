#filter() =: creates a collection of elements from an iterable for which a function returns true
# syntax: filter(function, iterable)

countries = [
   ("pakistan"),("turkey"),("usa","vito"),("india"),("russia","vito"),("UK","vito"),("china","vito"),("france","vito")
]

extract_V5= lambda country:country[1]=="vito" 

vitoPower = list(filter(extract_V5,countries))


for i in vitoPower:
   print(i)
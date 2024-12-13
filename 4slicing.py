name ="san joseph"

#slicing : two ways to do slicing
#indexing --> stringName[starting index: ending Index: step]
print(name[0:10])
print(name[0:5]) #first name
print(name[6:11]) #last name

reversed_name= name[::-1]
print(reversed_name) #how to reverse a string : using the slicing/indexing technique

#let we have list of webaddresses and we want to extract the just the websit names then slicing comes into play

website1 =  "https://google.com"
website2 =  "https://microsofbing.com"

slice=slice(8,-4)
 
print(website1[slice])
print(website2[slice])


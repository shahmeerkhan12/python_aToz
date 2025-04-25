# Dictionay: Dict in python is changeable and unordered data type that stores values in the form of key:value
# pairs, Furthermore it is fast as it works on the principles of hashing

# let create a dict for country and along with their universities
Country = {'England':'Oxford',
           'USA':'Cambridge',
           'India':'IIT',
           'Pakistan':'GIKI'
           }
           # we can do the following operations

#print(Country)

# print(Country.keys())

# print(Country.values())

# print(Country['Germany']) # since Germany does not exist if we want to check whther Germany exist or not

# print(Country.get('Germany'))

# to add Germany to the Dict
# Country.update({'Germany':'Berlin'})

# let remove india from the dict
# Country.pop('India')

# and ofCourse there is a clear method tooo
# Country.clear()

# print()
# for key,value in Country.items():
#    print(key, value)

# we are printing the keys only
for key in Country:
   print(key)
print()

# we are printing the values in the dict
for value in Country:
   print(Country.get(value))
# print()

# remember the Dict.keys() will return the keys in the dict if exists else default

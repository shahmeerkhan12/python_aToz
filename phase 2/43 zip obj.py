# zip(iterable1,iterable2,..........n):= aggregate elements from two different iterables
#     creates a zip object with paired elements stored in tuples for each element

usernames=["larau","byanci","grabich"]
passwords=("i!2dh998","byan11*$i","Garr322@1")
created = ('1/3/24','23/4/21','19/5/2019')

info = zip(usernames,passwords,created)
# type of zip
print(type(info))
# change type into any iterable (like list, tuple, dict, etc)
# info = list( zip(usernames,passwords,created))
# info = dict( zip(usernames,passwords,created))
# info = tuple( zip(usernames,passwords,created))
for i in info:
   print(i)
#duck typing = a scenario where the class type is less important than the methods or attributes
#             ->  class type is not checked if the minimum methods or attributes are present
#             ->   if it walks like a duck and it quacks like duck then it must be duck

class duck:
   def walk(self):
      print("this duck is walking")
   def talk(self):
      print("this duck is talking")

class Chiken:
   def walk(self):
      print("this chiken is walking")
   def talk(self):
       print("this chiken is cluking")

class person:
   def catch(self, duck):
      duck.walk()
      duck.talk()
      print("You caught the cripper")


duck1=duck()
chiken=Chiken()

person1=person()

#notice here that i have Passed the chiken object but the method accepts the class duck type objs
# this case is referred to as the duck typing
# here the attributes/methods are present in the class Chiken type objects therefore its methods are
# called without any error
# you would think that the it might execute the class duck type methods but the case is opposite, class
# type does really matter, but the as these methods are also present in the chiken type, therefore
# they are executed
person1.catch(chiken)
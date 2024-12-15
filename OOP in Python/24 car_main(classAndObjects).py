from car import Car # including the class Car
from car import Sports 
car_1=Car("ford","B12wh","blue",2019)
car_2=Car("honda","mustang","black",2010)
# car_1.drive()
# car_2.start()

# BY default all objects will have the default class wheels = 4

# we can access the class variables wheels as

print(Car.car_wheels)
print(car_1.car_wheels)
print(car_2.car_wheels)
print(car_1.drive())

# let if want to change the wheels to 2 for motorbike

motorbike = Car("bike","two_seater","blue",2020)

motorbike.car_wheels=2
print(motorbike.car_wheels)
print(motorbike.start())



# sports class operations
sport1 = Sports("Football","cricket")
sport1.famousSport()
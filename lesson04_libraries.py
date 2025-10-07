import math


print("Sqroot:", math.sqrt(144))
print("Rnd Up:", math.ceil(6.7))
print("Rnd Dwn:", math.floor(4.2))
print("Pi:", math.pi)
print("Power:", math.pow(2,5))

seed=994.2421
endnum=11

if endnum>10:
    math.ceil(endnum-1)

if endnum<1:
    math.ceil(endnum)

print(endnum)


import random

#methodz
print(random.randint(6,7))
print(random.random())
mylist=["e g g", "c h e e b n u r g e r", "6","7"]
print(random.choice(mylist))
random.shuffle(mylist)
print(mylist)

radius=14/2
circle_area=(math.pi*radius**2)
print(circle_area)

die_roll=random.randint(1,6)
print(die_roll)
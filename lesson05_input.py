name=input("Enter Username:")
print("Welcome back,",name)

age=int(input("Enter current age:"))
print(age)

import math
color=input("Enter favorite color:")
print(color)


print("Give two numbers to add:")
num1=int(input("Number 1:"))
num2=int(input("Number 2:"))
print(num1+num2)

diameter=int(input("Please give me a circle diameter:"))
area=math.pi*(diameter/2)**2
print(area)

import random
dicenumb=int(input("How many sides:"))
randnumb=random.randint(1,dicenumb)
print("Your number is...",randnumb)
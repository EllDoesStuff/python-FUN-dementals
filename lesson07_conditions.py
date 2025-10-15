# CONDITIONALS IN PYTHON
# comparison operators: ==, !=, <, >, <=, >=
# logical operators: and, or, not
# control flow: if, elif, else

print()
print("--- Conditionals in Python ---")
# Boolean refresher:
print( 3 == 2 )
print("Hello" == "Hi there")
print( 7 != 4)
print(4 > 5)

# if
num1 = 10 
if num1 == 10: 
    print("Your number is equal to 10")

num2 = 11
print(num2 <= 12)
if num2 <= 12:
    print("Your number is less than or equal to 12")    
else: 
    print("Your number is greater than 12")

    #if elif else

temperature = 72
if temperature > 80: 
    print("It's hot!")
elif temperature >= 60:
    print("It's nice.")
else:
    print("It's cold!")

x = 20 
y = 20

if x == y:
    print("good")
elif x > y:
    print("x is greater than y")
elif x < y: 
    print("x is less than y")
else: 
    print("error")

# Logical operator: and
# Both sides of the 'and' must  be true, otherwise it's false. 

# Logical operator: and
# Both sides of the 'and' must  be true, otherwise it's false. 
print()
print()
print()

age = 16
has_permission = True

if age >= 17 and has_permission:
    print("You can drive")
else:
    print("Can't drive yet")

# Using 'or' and 'not'
print("--- Using 'or' --- ")
day = "Monday"

if day == "Saturday" or  day == "Sunday":
    print("It's the weekend!")
elif day == "Monday" or day == "Tuesday":
    print("It's Monday or Tuesday")
else:
    print("It's Wed,Thur, or Fri")

if day is not "Monday":
    print("It's not Monday")

# numbah = int(input("Please enter a number:"))    
# evenodd = numbah % 2
# if evenodd == 1:
#     print("ts oddballz")
# else:
#     print("ts even")

# passwrd = "GYROZEPPELI"
# whatpasswrd = input("Please enter password:")
# if passwrd == whatpasswrd:
#     print("Access Granted, Manchacho")
# else:
#     print("Access Denied, Brorito")

grados = int(input("Please enter a grade:"))
if grados>=90:
    print("You got an A!")
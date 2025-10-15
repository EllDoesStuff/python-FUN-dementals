greeting="Hello"
name="Ada"
print(greeting,name)

# 0 1 2 3 4 
# H e l l o
print(greeting[1])

message = greeting + " " + name + "!!!"
print(message)

beegword = "Super-cali-fragil-istic-expi-ali-docious"
print("First letter:", beegword[0])
print("Last letter:", beegword[-1])
print("Reversed:", beegword[::-1])
print("What you are:", beegword[:5])
print("Range of letters (non-inclusive):", beegword[-7:-2])
print("Last seven letters:", beegword[-7:])
print("Step through every second character:", beegword[::2])

country = "Austrailia"
length_of_word = len(country)
print(length_of_word)

#a friend in len()

phrase = "SpOnGEBob SQuarePanTs"
print("Uppercase:", phrase.upper())
print("Lowercase:", phrase.lower())
print("Capitalize:", phrase.capitalize())
print("Title Format:", phrase.title())

#find and replace text
sentence = "ARE YOU READY TO NERD OUT?"
new_sentence = sentence.replace("ARE YOU", "I'M")
newnew_sentence = sentence.replace("?", "!")
print(sentence)
print(newnew_sentence)


print("\n--- Formatted Strings ---")

name = "Ada"
age = 28
city = "London"

print(f"Hello, my name is {name}. I am {age} years old and live in {city}.")
print(f"Next year I'll be {age + 1}. My name in uppercase is {name.upper()}.")

# quote = input("What is your favorite quote?")
# print(f"Your quote is {len(quote)} characters long.")

# first = input("First name:")
# last = input("Last name:")
# print(last + "," + first)

word = input("Please give me a word.")
print(word.upper())
print(word.lower())
print(word.capitalize())
print(word[::-1])
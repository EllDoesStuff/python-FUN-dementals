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

phrase = "SpOnGEBob"
print("Uppercase:", phrase.upper())
print("Lowercase:", phrase.lower())
print("Capitalize:", phrase.capitalize())
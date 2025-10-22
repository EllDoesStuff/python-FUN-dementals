print("--- Lists in Python ---")

#initialize a list with brackets:
empty_list = []
empty_list.append("Thing")
print(empty_list)

animals = ["donkey", "pangolin", "blobfish"]
numbers = [2, 4, 6, 8, 10]
mixed = ["piffle", 42, True, 9.99]

print(animals)
print(numbers)
print(mixed)

print("--- Indexing: how to access the elements of a list ---")
print("First Element:", animals[0])
print("Second element:", animals[1])
print("Last element:", animals[-1])


print("--- Modifying Lists ---")
animals[0] = "babirusa"
print(animals)

animal_to_replace = animals.index("pangolin")
print(animal_to_replace)
animals[animal_to_replace] = "seamonkey"

animals.append("glass frog")
print(animals)

# add element at end:
animals.append("glass frog")
print(animals)

# insert element at specific index
animals.insert(3, "aye-aye")
print("Inserted one animal:", animals)
animals.insert(1, "camel")
print("Inserted another animal:", animals)

animals.remove("babirusa")
print(animals)

last_animal = animals.pop()
print("Removed animal:", last_animal)
print("Remaining animals:", animals)

nums = [3, 7, 1, 9, 4, 2, 5, 8, 6, 0]
print("Original Numbers:", nums)
print("Length of the list:", len(nums))
print("Min:", min(nums))
print("Max:", max(nums))
print("Sum:", sum(nums))

nums.sort()
print(nums)
animals.sort()
print(animals)

print("--- Checking Membership ---")

if "cat" in animals:
    print("Cat is in the list!")
else:
    print("Cat is not in the list.")

if "cat" in animals:
    print("Cat is in the list!")
else:
    print("Cat is not in the list.")


print("--- Copying Lists ---")

original_list = [1, 2, 3]
copied_list = original_list
copied_list = original_list.copy()
copied_list.append(4)
print(original_list)
print(copied_list)

print()
print("--- Nested Lists/The Matrix ---")
matrix = [
[1,2,3], 
[4,5,6], 
[7,8,9]  
] 

print(matrix[0][2])

# varlyst = [1,2,3,4,5,6]
# newnumbergh = input("Please enter a new integer:")
# varlyst[2] = newnumbergh
# print(varlyst)

# Initialize an empty list called `shopping`.
# Add three items of your choice using `.append()`.
# Then insert one extra item at the second position 
# Remove one item of your choice.
# Finally, print the final shopping list.

shopping = []
shopping.append(input("Please enter an item:"))
shopping.append(input("Please enter an item:"))
removeit = shopping.append(input("Please enter an item:"))
shopping.insert(1, input("Please enter an item:")) 
animals.remove(removeit)
print(shopping)
# Write an algorithm that takes a string and returns True if it's a palindrome 
# (reads the same forward and backward), otherwise False.

palindroming = input("Please input possible palindrome:")
print(palindroming == palindroming[::-1])

# Write an algorithm that takes a string.
# If the string is at least 3 characters and doesn’t end with "ing", add "ing".


# If it does end with "ing", add "ly".


# If it's less than 3 characters, return it unchanged.


wordappend = input("Please enter word:")


wordsubtract = len(wordappend)
wordval = wordsubtract - 3
wordval2 = wordappend[wordval:wordsubtract]


if wordval2 == "ing":
    print(f"New word: {wordappend[0:wordval]}ly ")

elif len(wordappend) >= 3 and wordval2 != "gni":
    print(f"New word: {wordappend}ing.")
else:
    print(wordappend)

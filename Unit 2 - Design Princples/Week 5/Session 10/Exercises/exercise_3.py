# Exercise 3

# A palindrome is a word, number or other sequence of characters which reads the same backward or forward, such as madam or kayak.

# Write a function that takes a string and determines whether it's a palindrome or not. The function should return a boolean (True or False value).

str = input("Type in a palindrome: " )

def palindrome_finder(str):
    # Check if string entered is the same reversed. 
    # Returns True or False
    return str == str[::-1]

# Result is what is the output of this function
result = palindrome_finder(str)
 
# Check if result (True or False) is a palindrome.
if result:
    print("Yes, this is a palindrome.")
else:
    print("No, this is not a palindrome.")

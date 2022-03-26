# Python Bootcamp  Day 2:
# Fundamentals of Python
# https://www.youtube.com/watch?v=j_ietmzBsnI&feature=youtu.be

# Identation

if 5 > 2 :
    print("five is greater than 2")

# Variables (case-sensitivity)

myvar = 4
my_var = "Hello"
_my_var = True

# Python comment

# Camelcase
pythonBootcamp = "Welcome to Niyo!" # new comment
# snakecase
disrupt_bootcamp = "Software Architecture"
# Pascalcase
ILovePython = "Hello World!"

# Multi-line comment
"""
Hello first line of comment
second
third
"""

# Casting

var = "5"
type(var) # string

var = int(var)
type(var) # type has now changed to int


number_of_hours = int()

height = int(150.0)
type(height)

# Global and local scoping

name = "Sandra" # varible is defined globally so it can be accessed anywhere

def print_name():
    name = "Sandra" # only defined locally, can only be accessed within this function
    pass
    print(f"Hello, my name is {name}")
print_name()

# Python Data Types



# Python Arithmetic Operations

num = 5 + 6 # Addition
num -2 # Subtraction
num * 5 # Multiplication
num / 10 # Division

age = 50
age % 12 # Modulus

dog = 3
dog ** 4 # Exponential

newNum = 12
num // 4 

# Comparison operators

num == 4 # Outputs boolean True or False

num != 15

num < 6

nuum > 5

num <= 17



# Logical Operators

age1 = 25
age2 = 30

age > 20 and age2 > 35 # False

age > 20 or age2 > 35 # True

not(age > 20 or age2 > 35) # False

# Membership Operation

names = ["David", "Oluchi", "Ope", "Yemi"]
print(names)
"David" in names
"Cynthia" in names

# Task 4

numberInput = int(input("Enter a number: "))
numberInput = numberInput + 2
print("Your new number is: ", numberInput)

# Task 5

input_1 = int(input("Enter a the first number: "))
input_2 = int(input("Enter a the second number: "))
input_3 = int(input("Enter a the third number: "))
input_4 = int(input("Enter a the fourth number: "))
input_5 = int(input("Enter a the fifth number: "))

print(f"{input_1},{input_2},{input_3},{input_4},{input_5}", sep="   ")

# Task 6

user_fname = input("Enter your name: ")
user_age = int(input("Enter your age: "))
dog_age = (user_age*15)
print(f'Hello {user_fname}, you are {dog_age} years old, in Dog years.')

# Task 7

length = int(input("Enter your length of the field: "))
width = int(input("Enter your width of the field: "))
area = length * width
perimeter = 2*(length+width)
print(f"The length of the field is {length}. The width of the field is {width}. The area is: {area}. The perimeter is {perimeter}.")

# Python List

food = ["Rice", "Beans", "Pasta", "Bread"]
food.append("Plantain") # ["Rice", "Beans", "Pasta", "Bread", "Plantain"]

new_food = food.copy() # Copy list and save in a new list

food.index("Beans") # Find the index of an item

food.insert(2, "Stew") # Insert item at specfied index

food.pop(1) # Remove item from list using index

food.remove("Bread") # Remove value from list

removed_food = new_food.remove("Beans") # Remove item from list and store in a variable

food.sort() # Sort list alphabetically

food.clear() # Clear all values from list

fav_foods = ["Rice", "Orange", "Beans", "Pineapple"]

new_food.extend(fav_foods) # Combine both lists

new_food.count("Rice") # Count how many of an item
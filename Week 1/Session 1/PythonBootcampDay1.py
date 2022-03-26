# Python Bootcamp  Day 1:
# Fundamentals of Python
# https://www.youtube.com/watch?v=0EV0yz-9Sco

# Creating a variable called name
name = "Sandra"

# Creating a variable that contains your interests
interests = "I am interested in Agile Delivery, specifically SaaS. I am also interested in SQL."

# Print name variable to the terminal
print(name)

# Print interests variable to the terminal
print(interests)

# Print name and interests variable to the terminal
print(name,interests)

type("London")

type(3)

type(True)

type(3142)

type(1000000)

type(1+2j)

type(-3)

type(False)

type(0)

type("Social Distancing")

a = 7 * 3/2
print(a)

b = 7.3 / 2 
print(b)

c = 7//2
print (c)

d = 7 % 2
print(d)

e = 7 ** 2
print (e)

f = 7 +2/3**2-5
print(f)

g = "python" + "bootcamp"
print(g)

"python" + 3 # Can't concatenate string to number

"python" + "3"

"python" * 3

3 * "python"

"I love" + "" + "python" * 3

"I love" * 3 + "python"

("I love python") * 3

myvariable = "I love python"
MyVariable = "I hate python"
MYVARIABLE = "I am learning python"

print(myvariable)
print(MyVariable)
print(MYVARIABLE)

print('The value of 3+4 is', 3+4)

print('A', 1, 'KYE', 2)

age = 26
print(f"my age is {age}")

print(f"Ten multiplied by ten is {10*10}")

name = input("Enter your name: ")

print(name)

age = input("Enter your age: ")
type(age) 

age = int(input("Enter your age: "))
type(age) 

# Task 1

welcomeUser = input("Enter your name: ")
print(f"Welcome {welcomeUser}")
print(f"Welcome {welcomeUser}, your age is {age}")

# Task 2

height = int(input("Enter your height in inches: "))
weight = int(input("Enter your weight in pounds: "))
bmi = 703 * (weight/(height*height))
print(f"Your weight is {weight} and your height is {height} and therefore your BMI is {bmi}")


height = int(input("Enter your height in inches: "))
weight = int(input("Enter your weight in pounds: "))
print("Your BMI is ", 703 * (weight/(height*height)))

# Task 3

userName = input("Enter your name here: ")
print("Your name 3 times is: ", userName*3)
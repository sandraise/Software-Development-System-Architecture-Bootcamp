# Python Bootcamp  Day 4:
# Fundamentals of Python
# https://www.youtube.com/watch?v=Jv3wMfMf1m8

num1 = 5
num2 = 8

if (num1 > num2):
  print("This is true")
else:
  print("This is not true")

bank_balance = 10
access_code = "niyo"

user_input_price = int(input("Enter the price of product: "))
user_input_access_code = input("Enter the access code: ")

if bank_balance < user_input_price or user_input_price != access_code:
  print("Card declined.")
else:
  print("Payment accepted.")

for i in range(5):
  if i < 3:
    print("Hello World")
  else:
    print("Hi World")

# Print odd numbers between 1 to 10
for i in range(1,10,3):
  print(i)

# Print odd numbers between 1 to 20
for i in range(1,20,2):
  print(i)

# Iterating through a list
list = [382,372,6683,8361,393]

for i in list:
  print(i*2)

my_tuple = ("Yellow", "Pink", "Purple", "Blue")

for i in my_tuple:
  print(f'My favourite colour is', i)

# Write a program that will print ‘A’, then ‘B’, then it will alternate C's and D's five times and then finish with the letter E once.

print("A")
print("B")
for i in range(5):
  print("C")
  print("D")
print("E") # This is outside the for loop

cars = {
"car1" : {"brand": "Dodge", "model": "Black Mamba", "year": 2019},
"car2" : {"brand": "Mercedes", "model": "Classics", "year": 1905},
"car3" : {"brand": "Tesla", "model": "CS50", "year": 2025}
}

for i in cars['car1'].values(): # Specify which to loop through
  print(i)

for i in cars['car3'].keys():
  print(i)

# Simple function
def simple_func(name):
  return(f"Hello, how are you {name}?")

simple_func("Sandra")

# Convert miles to km


def dis_converter():
  miles = int(input("Enter miles: "))
  kilometers = miles * 1.6
  return(f"Miles is: {miles}. Kilometers is {kilometers}") 

dis_converter()
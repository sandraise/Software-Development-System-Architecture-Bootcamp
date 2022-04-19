# Python Bootcamp Day 7:
# Fundamentals of Python
# https://youtu.be/6Ikc90qunJs

# Create Parrot class with properties and methods
class Parrot:

    # class attribute
    species = "bird"

    def __init__(self,name,age):

        # instance attribute
        self.name = name
        self.age = age

    def talk(self):
        return "I am a talking parrot."

    def sing(self,song):
        return "{} sings {}".format(self.name, song)
    
    def dance(self):
        return "{} is now dancing".format(self.name)

# Instantiate Parrot
blu = Parrot("Blu", 10)
woo = Parrot("Woo", 15)

# access the class attributes

def demo_print():
    print("Hello World")

if "__name__" == "__parrot__": 
    print("Blu is a {}".format(blu.__class__.species))
    print("Woo is a also a {}".format(woo.__class__.species))

    # access the instance attributes
    print("{} is {} years old".format(blu.name,blu.age))
    print("{} is {} years old".format(woo.name,woo.age))

    # Instance methods
    print(blu.sing("Happy"))
    print(woo.dance())
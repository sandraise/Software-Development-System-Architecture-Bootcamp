# Python Bootcamp Day 9:
# Design Principles
# https://www.youtube.com/watch?v=Zv2RbaLfjCs

# Create Bird class
class Bird:
    # Bird class methods
    def __init__(self,name,age,specie,breed):
        self.__name = name
        self.age = age
        self.specie = specie
        self.__breed = breed

    def whoisThis(self):
        return "Hello, I am a Bird."

    def swim(self):
        return "I can swim"

# bella = Bird()
# print(bella.whoisThis())
#print(bella.name)

# Create Penguin class that inherits the Bird class properties
class Penguin(Bird):

    def __init__(self,name,age,colour,specie,breed):
        super().__init__(name,age,specie,breed)
        # self.colour = colour
        # return "I am a Bird type Penguin"

    def run(self):
        return "I am running"

class Pelican(Bird):

    def walk(self):
        return "Walk slowly"

brd = Bird("Birdy",12,"Mixie")
pen = Penguin("Peggy",63,"Red","Flying bird","Mixie")

print(pen.name)

print(pen.__name)

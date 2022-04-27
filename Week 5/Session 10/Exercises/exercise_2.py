# Exercise 2

# Create three classes of animals: Terrestrial, Aquatic and Amphibian
# Define properties- name, 
# methods: 
#         Aquatic - can_swim
#         Terrestrial - can_walk
#         both - GREET: I am 'name of animal' of the 'sea or/and land'

# Amphibian - Should inherit the properties and methods of the previous classes 

class Terrestrial:
    def __init__(self,name,land):
        self.name = name
        self.land = land

    def can_walk(self):
        return "I can walk."
    
    def greet(self):
        return("I am {} of the {}".format(self.name,self.land))

terry = Terrestrial("Terry","land")
print(terry.greet())
print(terry.can_walk())

class Aquatic:
    def __init__(self,name,land):
        self.name = name
        self.land = land

    def can_swim(self):
        return "I can swim."

    def greet(self):
        return("I am {} of the {}".format(self.name,self.land))

aqua = Aquatic("Aqua", "sea")
print(aqua.greet())
print(aqua.can_swim())

class Amphibian(Terrestrial,Aquatic):
    def __init__(self,name,land):
        self.name = name
        self.land = land

amy = Amphibian("Amy", "sea and land")
print(amy.greet())
print(amy.can_swim())
print(amy.can_walk())


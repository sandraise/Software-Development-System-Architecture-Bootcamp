# Python Bootcamp Day 10:
# Design Principles
# 

class Parrot:

    def fly(self):
        print("Parrot can fly")

    def swim(self):
        print("Parrot can't swim")

class Penguin:

    def fly(self):
        print("Penguin can't fly")

    def swim(self):
        print("Penguin can swim")

# Common interface
def flying_test(bird):
    bird.fly()

# Instantiate objects
blu = Parrot()
peggy = Penguin()

flying_test(blu)
flying_test(peggy)
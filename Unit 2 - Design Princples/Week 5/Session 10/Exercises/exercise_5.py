# Exercise 5

# Write a program which mimicks the different sounds made by animals and your program should return your desired error message for an animal sound you have not implemented.

#animalInput = input("Type in an animal: ")

class Dog:
    
    def animal_sound(self):
        return "Bark!"

class Cow:

    def animal_sound(self):
        return "Mooo!"

class Cat:

    def animal_sound(self):
        return "Meeeoow!"

class Snake:
    
    def animal_sound(self):
        return "Ssssss!"

def animal_speak(sound):
    print(sound.animal_sound())

dog_1 = Dog()
cat_1 = Cat()
cow_1 = Cow()
snake_1 = Snake()

animal_speak(dog_1)
animal_speak(cat_1)
animal_speak(cow_1)
animal_speak(snake_1)
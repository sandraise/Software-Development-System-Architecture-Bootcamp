# Exercise 5

# Write a program which mimicks the different sounds made by animals and your program should return your desired error message for an animal sound you have not implemented.

animalInput = input("Type in an animal: ")

def animal_sounds(animal):
    if animal.lower()=="dog":
        return ("Bark!")
    elif animal.lower()=="cat":
        return ("Meow!")
    elif animal.lower()=="cow":
        return ("Moo!")
    elif animal.lower()=="snake":
        return ("Ssss!")
    else:
        return ("I do not know that animal. Plese try again.")

print(animal_sounds(animalInput))
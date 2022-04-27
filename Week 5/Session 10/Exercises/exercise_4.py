# Exercise 4

# Write a class with different methods, first-returns the first and last items of your input when the method is called and second method shouid return the middle item(s)

class Flower:
    def __init__(self,name,petals,stem,leaf):
        self.name = name
        self.petals = petals
        self.stem = stem
        self.leaf = leaf
    
    def favourite_flowers(self,list):
        # Find the first item = index 0
        # Find the last item = index -1
        first_last = [list[0],list[-1]] 
        return(f"The first and last items are: {first_last}")
    
    def least_favourite_flowers(self,list):
        # The middle is the length of the list e.g. total elements divided by 2
        middle = list[int(len(list)/2)]
        return(f"The middle item is: {middle}")

flower = Flower("Sunflower", 5, 4, 2)
print(flower.favourite_flowers(["Rose","Daffodil","Sunflower","Tulip","Lily","Daisy","Lavender","Violet"]))
print(flower.least_favourite_flowers(["Rose","Daffodil","Sunflower","Tulip","Lily","Daisy","Lavender","Violet"]))
# Create a class Vehicle of type sports car for all cars you create that names a speed, colour, can drift

# Create Vehicle class
class Vehicle:

    # Class attributes
    type = "sports car"

    def __init__(self,model,colour,speed,rim_colour):

        # Instance attributes
        self.model = model
        self.colour = colour
        self.speed = speed
        self.rim_colour = rim_colour
    
    # Class methods
    def drift(self,speed):
        return ("{} can drift very well because my speed is {}".format(self.model,self.speed))

    def accelerate(self,rim_colour):
        return "{} can accelerate, it has {} colour rims!".format(self.model,self.rim_colour)

# Create instance of Vehicle class
ferrari = Vehicle("Ferrari","Black","200mph","Silver")

# Call instance methods
print(ferrari.drift("200mph"))
print(ferrari.accelerate("Yellow"))

# Call class attribute
print(ferrari.type)

# Access instance attributes
print("{} is {} in colour with {} rims and can go up to {} ".format(ferrari.model,ferrari.colour,ferrari.rim_colour,ferrari.speed))

# Access class attribute
print("{} is a type of {}".format(ferrari.model,ferrari.__class__.type))
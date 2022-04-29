# Create Bird class
class Bird:
    # Bird class methods
    def __init__(self,name):
        # Passing a name attribute
        self.name = name;
        print("Hi, I am a bird.")

    def whoisThis(self):
        return "Bird"

    def swim(self):
        return "Swim faster"
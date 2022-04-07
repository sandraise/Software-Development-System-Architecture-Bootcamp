# Create Car class

class Car:
    # Add methods
    def __init__(self,model,colour):
        self.model = model
        self.colour = colour

    def drive_forward(self):
        return("Moving forward...", {self.colour})

# Instantiate Car class
car1 = Car("CR7","White")
car2 = Car("Nissan","Black")
print(car1.model)
print(car1.drive_forward())

# Create the instance attributes fullname and email in the Employee class. Given a person's first and last names:

# Form the fullname by simply joining the first and last name together, separated by a space.
# Form the email by joining the first and last name together with a . in between, and follow it with @company.com at the end. Make sure the entire email is in lowercase.

class Employee:
    # Initialising the Employee class with attributes of first and last name
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    # Creating a method that uses Employee class and returns the first and last name
    def fullname(self):
        return self.firstname + " " + self.lastname

    # Creating a method that uses Employee class and creates an email
    def email(self):
        return self.firstname.lower() + "." + self.lastname.lower() + "@company.com"

# Instantiating the Employee class and defining parameters

emp_1 = Employee("John", "Smith")
emp_2 = Employee("Mary",  "Sue")
emp_3 = Employee("Antony", "Walker")

# Calling the functions

print(emp_1.fullname())
print(emp_1.email())

print(emp_2.fullname())
print(emp_2.email())

print(emp_3.fullname())
print(emp_3.email())
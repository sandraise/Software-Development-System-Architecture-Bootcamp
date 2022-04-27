# Exercise 1

# Luke Skywalker has family and friends. Help him remind them who is who. Given a string with a name, return the relation of that person to Luke.

# **Person	        Relation**
# Darth Vader	    father
# Leia	            sister
# Han	            brother in law
# R2D2	            droid

def relation_to_luke(str):
    if str.lower()=="darth vader":
        print("Luke, I am your father.")
    elif str.lower()=="leia":
        print("Luke, I am your sister.")
    elif str.lower()=="han":
        print("Luke, I am your brother-in-law.")
    elif str.lower()=="r2d2":
        print("Luke, I am R2D2.")
    else: 
        print ("I do not know who you are.")

relation_to_luke("Darth Vader")
relation_to_luke("Leia")
relation_to_luke("Han")
relation_to_luke("R2D2")
relation_to_luke("Sandra")
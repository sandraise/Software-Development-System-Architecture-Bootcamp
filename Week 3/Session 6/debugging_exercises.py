# EXERCISE 1

def cubes(x):
    return x**3

print(cubes(3))
print(cubes(5))
print(cubes(10))

## EXERCISE 2

current_time_str = input("What is the current time (in hours 0-23)?")
wait_time_str = input("How many hours do you want to wait")

current_time_int = int(current_time_str)
wait_time_int = int(wait_time_str)

final_time_int = current_time_int + wait_time_int
print(final_time_int)

# EXERCISE 3

def increment_items(list):
    for i in list:
	    i += 1
    return list

print(increment_items([0, 1, 2, 3]))
print(increment_items([2, 4, 6, 8]))
print(increment_items([-1, -2, -3, -4]))

## EXERCISE 4

def name_string(name):
    b = "BlackDisrupt"
    result = name + b
    return result

print(name_string("Mercy"))
print(name_string("Sandra"))
print(name_string("Python"))
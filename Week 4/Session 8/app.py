from car import create_car
import car
import sys
sys.path.append('../')
import parrot as bird


tesla = car.Vehicle("GHG","Black",210,"Yellow")
print(tesla.model)
print(tesla.colour)
print(car.ferrari.drift("200mph"))

print(bird.blu.dance())

print(create_car())
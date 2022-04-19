from car import create_car
import car
import sys
sys.path.append('/Users/sandraise/Desktop/Software Development & System Architecture Bootcamp/Week 4/Session 7')
# sys.path.append('../')
# print(sys.path)
import parrot as bird


tesla = car.Vehicle("GHG","Black",210,"Yellow")
print(tesla.model)
print(tesla.colour)
print(car.ferrari.drift("200mph"))

print(bird.blu.dance())

print(create_car())
from app_1 import location_finder as lf
from app_1 import food_finder as ff
import random
import math
import datetime

places = ["Abuja", "New York", "London", "Hawaii"]

print(lf(places,"London"))

print(lf(places,"Accra"))

snacks = ["Puffpuff", "Popcorn", "Biscuits", "Marshmallows"]

print(ff(snacks,"Icecream"))

print(ff(snacks,"Popcorn"))

print(random.choice(places))
print(random.randint(1,10))
print(math.pi)

print(dir(math))

print(datetime.datetime.today())
print(datetime.datetime.now())
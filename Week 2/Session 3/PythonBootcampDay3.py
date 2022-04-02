# Python Bootcamp  Day 3:
# Fundamentals of Python
# https://www.youtube.com/watch?v=Zm_3q8MlXXk

countries = ['Nigeria', 'Ghana', 'UK', 'US', 'Canada', 'Libya', 'Germany']
type(countries)

len(countries)

# Selecting from first to the 4th element
countries[:4]

# Selecting from 3rd item to the end
countries[3:]

# Selecting last 6 items
countries[-6:]

countries[1:]

countries[1:5]

countries[4]

ages = [12,45,21,45,21,56,25,78]
ages

ages[2:7]

max(ages)

min(ages)

max(countries)

min(countries)

countries[3] = 'Algeria'
countries

p1, p2, p3 = ['Bed', 'Pillow', 'Mattress']
print(p1)
print(p2)
print(p3)

Tuples

new_tuple = tuple(countries)
type(new_tuple)

my_tuple = (("kia", "lexus", 3, True))
my_tuple

my_tuple[0]

t1, t2, t3, t4 = my_tuple
print(t1)
print(t2)
print(t3)
print(t4)

y1 = 'Kia'
y2 = 'lexus'

var = "disruptbootcamp"
var

var[:7]

var[7:]

num_1,num_2 = [1,2]
print((num_1+num_2)/2)

age1, age2 = ag



eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
eclipse_dates[-3:]

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]
q1 = days_in_month[:3]
print(q1)
q2 = days_in_month[3:6]
print(q2)
q3 = days_in_month[6:9]
print(q3)
q4 = days_in_month[-3:]
print(q4)

a1,a2,a3 = q1
print(a1+a2+a3)

b1,b2,b3 = q2
print(b1+b2+b3)

c1,c2,c3 = q3
print(c1+c2+c3)

d1,d2,d3 = q4
print(d1+d2+d3)

eclipse_tuple = tuple(eclipse_dates)
eclipse_tuple

new_tuple_list = (*eclipse_dates,)
tp = list(new_tuple_list)
tp[0] = "Jamaica"
tp

count_eclipse = tuple(eclipse_dates)
count_eclipse

count_eclipse.count('July 11, 2010')

count_eclipse.index(2)

Sets

days_per_month = (21,37,38,26,39,37,38,73,21)
days_per_month

days_per_month = set((21,37,38,26,39,37,38,73,21))
days_per_month

days = set(countries)
days

len(days)

days.add("Holland")
days

days.remove("Germany")
days

days.union(days_per_month)
days
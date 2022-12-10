'''
    Dictionary Comprehention
'''
import random

dict1 = {}
#Traditional for dict iteration Example 1
for i in range(1, 11):
    dict1[i] = i * 2 
print(dict1)

# dict comprehention
# key: func(iter) for iter in iterable_object
dict2 = {i: i * 2 for i in range(1, 11)}
print(dict2)

#Traditional for dict iteration Example 2
countries = ['col', 'mex', 'bol', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1, 100)
print(population)

# dict comprehention for
# key: func() for iter in iterable_object
population2 = {country : random.randint(1, 100) for country in countries}
print(population2)

# Using zip function to create tuples
# [TODO] Look more into zip library
names = ['nico', 'zule', 'santi']
ages = [12, 56, 98]
print(list(zip(names, ages)))

# Create new dict with zip object using dict comprehention
# elem1: elem2 for (elem1, elem2) in zip(elem1, elem2)
new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)
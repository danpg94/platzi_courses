'''
    Dict Comprehention 2
'''

import random 
countries = ['col', 'mex', 'bol', 'pe']

# Create a dict with randomly generated populaations using dict comprehention
# key: func() for iter in iterable 
population = {country : random.randint(1, 100) for country in countries}
print(population)

# Create a dict with countries with a population higher than 20
# key: value for (key, value) in tuple_iterable if condition
result = {country: population for (country, population) in population.items() if population > 20}
print(result)

# Make a dict with the amount of vowels in a given string
text = 'Hola mundo'
# key: func(iter) for iter in iterable if condition
unique = { c: text.count(c) for c in text if c in 'aeiou'}
print(unique)
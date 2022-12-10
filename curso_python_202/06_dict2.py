import random 
countries = ['col', 'mex', 'bol', 'pe']

population = {country : random.randint(1, 100) for country in countries}
result = {country: population for (country, population) in population.items() if population > 20}
print(result)

text = 'Hola mundo'
unique = { c: text.count(c) for c in text if c in 'aeiou'}
print(unique)
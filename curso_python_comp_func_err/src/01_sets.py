'''
Sets:   Cannot be modified
        Do not have an order
        Does not allow duplicates
'''
# Defining sets
set_countries = {'col', 'mex', 'bol'}
print(set_countries)
print(type(set_countries))

# Does not allow duplicates
# output: {1, 2, 443, 23}
set_numbers = {1, 2, 2, 443, 23}
print(set_numbers)

# Allows different types of objects
set_types = {1, 'hola', False, 12.12}
print(set_types)

# Can be used for strings
set_from_string = set('hola')
print(set_from_string)

# Can convert tuple to set
set_from_tuples = set(('abc', 'cbv', 'as', 'abc'))
print(set_from_tuples)

# Can convert list to set, (removes duplicates)
numbers = [1, 2, 3, 1, 2, 3, 4]
set_numbers = set(numbers)
print(set_numbers)

# Can convert set to list
unique_numbers = list(set_numbers)
print(unique_numbers)
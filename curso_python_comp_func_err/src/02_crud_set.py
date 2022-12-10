'''
    CRUD on sets (create, read, update, delete)

'''

# Create using "{" and "]" brackets
set_countries = {'col', 'mex', 'bol'}

# Read: Size of set
size = len(set_countries)
print(size)

#Read: if an object exists in a set
print('col' in set_countries)
print('pe' in set_countries)

# Update: add elements to set
set_countries.add('pe')
print(set_countries)

# Update: add other sets to existing set
set_countries.update({'ar', 'ecu'})
print(set_countries)

# Delete: Removes element from set (KeyError if not found)
set_countries.remove('col')
print(set_countries)

# Delete: Removes element from set (does not throw KeyError if not found)
set_countries.discard('ar')
print(set_countries)

# Delete: Removes all elements from set()
# WARNING: A cleared set is not None!
set_countries.clear()
print(set_countries)
setIsNone= set_countries is None
setEqualsNone = set_countries == None
print(setIsNone)
print(setEqualsNone)
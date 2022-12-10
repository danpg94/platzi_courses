'''
    Set Operations:
        Union                   ( | )
        Intersection            ( & )
        Difference              ( - )
        Symmetric Difference    ( ^ )

        Using set methods or logic operators


'''
# Defining sets
set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# Union using set method 
set_c = set_a.union(set_b)
print(set_c)

# Intersection using set method
set_c = set_a.intersection(set_b)
print(set_c)

# Difference using set method
set_c = set_a.difference(set_b)
print(set_c)

# Symmetric Difference using set method
set_c = set_a.symmetric_difference(set_b)
print(set_c)



# Union using logic operators
set_c = (set_a | set_b)
print(set_c)

# Intersection using logic operators
set_c = (set_a & set_b)
print(set_c)

# Difference using logic operators
set_c = (set_a - set_b)
print(set_c)

# Symmetric Difference using logic operators 
set_c = set_a ^ set_b
print(set_c)
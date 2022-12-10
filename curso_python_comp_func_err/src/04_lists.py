'''
    List Comprehention

'''
numbers = []

#Traditional for list iteration 
for element in range(1, 11):
    if element % 2 == 0:
        numbers.append(element * 2)
print(numbers)

# List comprehention
# func(iter) for iterable in iterable_object if condition
numbers_v2 = [element * 2 for element in range(1, 11) if element % 2 == 0]
print(numbers_v2)


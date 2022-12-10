# Class 5:

numbers = []
#Forma tradicional 
for element in range(1, 11):
    if element % 2 == 0:
        numbers.append(element * 2)
print(numbers)

#Forma corta
numbers_v2 = [element * 2 for element in range(1, 11) if element % 2 == 0]
print(numbers_v2)


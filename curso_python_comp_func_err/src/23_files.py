'''
    Opening Files 
'''

file = open('./text.txt')

# Creates a string of all of the contes of the file
#print(file.read())

#readline is an iterable and returns the next line
print(file.readline())
print(file.readline())
print(file.readline())

# must always close the file with file_obj.close()
file.close()

# Alternative method of opening files w/o having
# to use close() method
with open('./text.txt') as file:
    for line in file:
        print(line, end='')
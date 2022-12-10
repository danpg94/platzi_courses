'''
    Writing in Files
'''

with open('./text.txt', 'w+') as file:
    for line in file:
        print(line)
    file.write('\nnuevas cosas en este archivo')
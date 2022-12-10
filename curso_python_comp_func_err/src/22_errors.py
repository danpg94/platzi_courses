'''
    Try/Except
        Python permits several excepts within a single try:
        These functions 'catches' errors when it executes, 
        does not let the program end if it reaches an error.
        
'''

try:
    print(0 / 0)
    assert 1 != 1, "Uno no es igual que uno" 
    edad = 10
    if edad < 18:
        raise Exception('No se permite menores de Edad')
except ZeroDivisionError as error:
    print(error)
except AssertionError as error:
    print(error)
except Exception as error:
    print(error)

print('Hola')
'''
    Errors in Python
    There are many Types of errors that stop execution
    once they are raised. The reserved word 'assert' 
    is used to verify a condition, if True, raises an
    AssertionError which can be used by the programmer
    to verify expected behavior from their modules/
    scripts/tests  
'''

# print(0 / 0)              # ZeroDivisionError
# print(result)             # NameError          

# assert condition          # if True, raises Assertion error
print('Hola')

suma = lambda x,y: x + y
assert suma(2,2) == 4 # Verifies if the result is correct
 
edad = 10
if edad < 18:
    raise Exception('No se permite menores de Edad')

print('Hola 2')
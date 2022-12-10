'''
    Iterables:
        Object that contains a number of 'countable'
        variable. When used with a 'next()', it returns
        it's next value. Example in code.

'''

# [TODO] learn more about __iter__ and __next__ 

my_iter = iter(range(1, 5))
print(my_iter)
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))

# WARNING if iterable runs out of items in the object
# a StopIteration error is raised

